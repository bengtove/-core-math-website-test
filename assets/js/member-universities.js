(function () {
  var activeTrigger = null;
  var scrollX = 0;
  var scrollY = 0;
  var previousStyle = null;

  document.querySelectorAll('.member-portrait-dialog').forEach(function (dialog) {
    dialog.querySelector('[data-member-portrait-close]').addEventListener('click', function () { dialog.close(); });
    dialog.addEventListener('click', function (event) {
      if (event.target === dialog) dialog.close();
    });
    dialog.addEventListener('close', function () {
      if (!previousStyle) return;
      Object.keys(previousStyle).forEach(function (key) { document.body.style[key] = previousStyle[key]; });
      previousStyle = null;
      window.scrollTo(scrollX, scrollY);
      if (activeTrigger) activeTrigger.focus({ preventScroll: true });
      activeTrigger = null;
    });
  });

  document.querySelectorAll('[data-member-portrait-trigger]').forEach(function (trigger) {
    var dialog = document.getElementById(trigger.getAttribute('data-member-portrait-trigger'));
    if (!dialog || typeof dialog.showModal !== 'function') return;
    trigger.addEventListener('click', function (event) {
      event.preventDefault();
      activeTrigger = trigger;
      scrollX = window.scrollX;
      scrollY = window.scrollY;
      previousStyle = {};
      ['position', 'top', 'left', 'width'].forEach(function (key) { previousStyle[key] = document.body.style[key]; });
      document.body.style.position = 'fixed';
      document.body.style.top = -scrollY + 'px';
      document.body.style.left = -scrollX + 'px';
      document.body.style.width = '100%';
      dialog.showModal();
      dialog.querySelector('.member-portrait-dialog__surface').scrollTop = 0;
      dialog.querySelector('[data-member-portrait-close]').focus({ preventScroll: true });
    });
  });
}());
