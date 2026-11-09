from pathlib import Path
from PIL import Image,ImageOps,PngImagePlugin
import yaml,json,hashlib,base64,io,html
import resvg_py
here=Path(__file__).resolve().parent; repo=here.parents[2]
photos=yaml.safe_load((repo/'_data/member_photographs.yml').read_text())
order=[30,46,33,31,34,39,42,38,44,37,40,35,43,36,45,32,41,None]
assert len(set(x for x in order if x))==17
W,H=2400,1080;gap=4;margin=6;cw=(W-2*margin-5*gap)/6;ch=(H-2*margin-2*gap)/3
# Normalised offsets across the available crop, editable per photograph.
focal={30:(.5,.6),31:(.55,.55),32:(.28,.5),33:(.5,.5),34:(.5,.4),35:(.5,.5),36:(.5,.5),37:(.5,.5),38:(.5,.5),39:(.65,.5),40:(.5,.5),41:(.5,.5),42:(.5,.5),43:(.5,.5),44:(.65,.5),45:(.5,.5),46:(.5,.5)}
s=[f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<title>Meet the 17 universities behind CoRE-Math</title>','<desc>17 approved university photographs and the CoRE-Math logo. Separate credits in ATTRIBUTION.md. Review copy; LinkedIn upload clearance remains unresolved.</desc>',f'<rect width="{W}" height="{H}" fill="white"/>'];register=[]
for pos,num in enumerate(order):
 x=margin+(pos%6)*(cw+gap);y=margin+(pos//6)*(ch+gap)
 if num:
  pid=f'CM-PH-{num:06}';meta=photos[pid];p=Path(meta['archive_path']);sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==meta['original_sha256'],pid;name=meta['university']
 else:
  pid='logo';meta={};p=repo/'assets/images/branding/core-math-mark.png';sha=hashlib.sha256(p.read_bytes()).hexdigest();name='CoRE-Math logo'
 im=ImageOps.exif_transpose(Image.open(p)).convert('RGB' if num else 'RGBA');ow,oh=im.size
 scale=max(cw/ow,ch/oh) if num else min(cw*.72/ow,ch*.72/oh);assert scale<=1
 fx,fy=focal[num] if num else (.5,.5);dw,dh=ow*scale,oh*scale;ix=x-(dw-cw)*fx;iy=y-(dh-ch)*fy
 # Embed full image at a practical editing resolution, never the old collage assets.
 im.thumbnail((1800,1800),Image.Resampling.LANCZOS);b=io.BytesIO();im.save(b,format='PNG' if not num else 'JPEG',**({} if not num else {'quality':96,'subsampling':0}));mime='image/png' if not num else 'image/jpeg'
 s += [f'<g id="cell-{pos+1}" data-photo-id="{pid}"><title>{html.escape(name)}</title><clipPath id="c{pos}"><rect x="{x}" y="{y}" width="{cw}" height="{ch}"/></clipPath>',f'<image x="{ix}" y="{iy}" width="{dw}" height="{dh}" clip-path="url(#c{pos})" xlink:href="data:{mime};base64,{base64.b64encode(b.getvalue()).decode()}"/></g>']
 register.append({'cell':pos+1,'row':pos//6+1,'column':pos%6+1,'id':pid,'university':name,'original_sha256':sha,'original_dimensions':[ow,oh],'scale':scale,'focal_point':[fx,fy]})
s.append('</svg>');svg='\n'.join(s);(here/'collage.svg').write_text(svg);png=resvg_py.svg_to_bytes(svg_string=svg);im=Image.open(io.BytesIO(png));info=PngImagePlugin.PngInfo();info.add_text('Description','Review collage; see ATTRIBUTION.md for per-photo licences and README.md for remaining publication issue.');im.save(here/'collage.png',pnginfo=info,optimize=True);im.resize((1200,540),Image.Resampling.LANCZOS).save(here/'preview.png');im.resize((390,176),Image.Resampling.LANCZOS).save(here/'mobile-preview.png');(here/'cell-register.json').write_text(json.dumps(register,ensure_ascii=False,indent=2))
print('Verified 17 original SHA-256 hashes; 18 cells; no enlargement; PNG 2400 × 1080.')
