#!/usr/bin/env ruby
# Preparation runs automatically in Actions; GitHub Pages needs no custom plugin.
require 'yaml'
require 'date'
require 'json'
require 'securerandom'
require 'digest'
require 'fileutils'
require 'open3'

module LinkedInFeed
  ROOT = File.expand_path('..', __dir__)
  def self.posts(root)
    Dir[File.join(root, '_posts', '*')].select { |p| File.file?(p) }.sort.map do |path|
      text = File.read(path)
      match = text.match(/\A---\s*\n(.*?)\n---\s*\n/m) or raise "Missing front matter: #{path}"
      [path, text, YAML.safe_load(match[1], permitted_classes: [Time, Date], aliases: false) || {}]
    end
  end

  def self.run(root = ROOT, prepare = false)
    baseline = JSON.parse(File.read(File.join(root, '_data/linkedin_history.json')))
    raise 'Historical baseline must retain all 53 unique IDs' unless baseline.size == 53 && baseline.uniq.size == 53
    entries = posts(root)
    if prepare
      entries.each do |path, text, data|
        next if data['linkedin_id']
        File.write(path, text.sub(/\A---\s*\n/, "---\nlinkedin_id: #{SecureRandom.uuid}\n"))
      end
      entries = posts(root)
    end
    ids = entries.map { |_, _, data| data['linkedin_id'] }
    raise 'Missing/invalid linkedin_id; run ruby scripts/prepare_linkedin.rb --prepare' unless ids.all? { |id| id.is_a?(String) && id.match?(/\A[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\z/) }
    raise 'Duplicate linkedin_id (do not copy an existing article ID)' unless ids.uniq.size == ids.size
    images = {}
    entries.each do |path, _, data|
      id = data['linkedin_id']
      raise "Use boolean linkedin: false, not a string: #{path}" if data.key?('linkedin') && ![true, false].include?(data['linkedin'])
      next if baseline.include?(id) || data['linkedin'] == false
      source = data.key?('linkedin_image') ? data['linkedin_image'] : data['image']
      next if source.nil? || source == false || source == ''
      raise "Image must be a URL string: #{path}" unless source.is_a?(String)
      ext = File.extname(source.split(/[?#]/).first).downcase
      type = {'.jpg'=>'image/jpeg', '.jpeg'=>'image/jpeg', '.png'=>'image/png', '.gif'=>'image/gif'}[ext]
      if source.start_with?('https://')
        images[id] = {'url'=>source, 'type'=>type} if type
        next # No remote downloads during preparation; unsupported remote formats omitted.
      end
      raise "Use an absolute /assets/ path or HTTPS image URL: #{path}" unless source.start_with?('/assets/') && !source.split('/').include?('..')
      input = File.join(root, source.delete_prefix('/'))
      raise "Missing image: #{source}" unless File.file?(input)
      if ext == '.avif'
        source = "/assets/images/linkedin/#{Digest::SHA256.file(input).hexdigest}.png"
        output = File.join(root, source.delete_prefix('/'))
        if prepare && !File.exist?(output)
          FileUtils.mkdir_p(File.dirname(output))
          # Write atomically: an interrupted/failed conversion must not leave a cached PNG.
          temporary = output + '.tmp.png'
          begin
            command = ['python3', '-c', 'from PIL import Image, ImageOps; import sys; im = ImageOps.exif_transpose(Image.open(sys.argv[1])); im.save(sys.argv[2], format="PNG")', input, temporary]
            stdout, stderr, status = Open3.capture3(*command)
            raise "AVIF conversion needs Python 3 and Pillow >= 11.3: #{stdout} #{stderr}" unless status.success?
            File.rename(temporary, output)
          ensure
            File.delete(temporary) if File.exist?(temporary)
          end
        end
        raise "Missing AVIF derivative; run --prepare: #{source}" unless File.file?(output)
        input = output
        type = 'image/png'
      end
      next unless type # SVG and other unsupported images are optional, not logo fallbacks.
      signature = File.binread(input, 12)
      valid = case type
      when 'image/png' then signature.start_with?("\x89PNG\r\n\x1a\n".b)
      when 'image/jpeg' then signature.start_with?("\xff\xd8\xff".b)
      when 'image/gif' then signature.start_with?('GIF87a', 'GIF89a')
      end
      raise "Image bytes do not match #{type}: #{source}" unless valid
      images[id] = {'url'=>source, 'type'=>type, 'length'=>File.size(input)}
    end
    target = File.join(root, '_data/linkedin_images.json')
    if prepare
      File.write(target, JSON.pretty_generate(images) + "\n")
    else
      raise 'Image manifest is stale; run --prepare' unless File.exist?(target) && JSON.parse(File.read(target)) == images
    end
    puts "LinkedIn metadata OK: #{entries.size} posts, #{baseline.size} historical exclusions, #{images.size} eligible images"
  end
end
if $PROGRAM_NAME == __FILE__
  require 'date'
  abort 'Usage: ruby scripts/prepare_linkedin.rb [--prepare]' unless ARGV.empty? || ARGV == ['--prepare']
  LinkedInFeed.run(LinkedInFeed::ROOT, ARGV == ['--prepare'])
end
