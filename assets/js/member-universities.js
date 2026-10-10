(function () {
  var activeTrigger = null;

  document.querySelectorAll('[data-member-portrait-trigger]').forEach(function (trigger) {
    var dialog = document.getElementById(trigger.getAttribute('data-member-portrait-trigger'));
    if (!dialog) return;

    var closeButton = dialog.querySelector('[data-member-portrait-close]');

    trigger.addEventListener('click', function () {
      activeTrigger = trigger;
      dialog.showModal();
      closeButton.focus();
    });

    closeButton.addEventListener('click', function () {
      dialog.close();
    });

    dialog.addEventListener('click', function (event) {
      if (event.target === dialog) dialog.close();
    });

    dialog.addEventListener('close', function () {
      if (activeTrigger) activeTrigger.focus();
      activeTrigger = null;
    });
  });
}());
