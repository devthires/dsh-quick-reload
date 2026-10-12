/**
 * Client half of dsh-quick-reload.
 *
 * Binds plain F5 to a full page reload of the Harness Web client. A reload
 * rebuilds the renderer, which discards the per-session skill catalog cache in
 * `dsh-client-ui-skill` (`ctx.on('connection/reset', clearAll)` fires on boot),
 * so a skill installed on disk becomes visible in the `/` menu without
 * restarting the whole application.
 *
 * The listener is registered in `apply` through `ctx.effect`, so cordis
 * disposes it with the plugin and the factory itself stays side-effect free.
 */
window.__ModuleLoader__.load({
  id: 'dsh-quick-reload',
  factory() {
    return {
      apply(ctx) {
        ctx.effect(() => {
          const onKeyDown = (event) => {
            // Plain F5 only: never shadow the modified variants a user may
            // have bound elsewhere (Ctrl+F5, Shift+F5, ...).
            if (event.key !== 'F5') return;
            if (event.ctrlKey || event.altKey || event.metaKey || event.shiftKey) return;
            if (event.repeat) return;
            // Stop any browser-level default (Electron binds none here, but a
            // future host change must not turn this into a double reload).
            event.preventDefault();
            window.location.reload();
          };
          // Capture phase, so the reload wins regardless of which element owns
          // focus (composer, terminal, a dialog input, or the page body).
          window.addEventListener('keydown', onKeyDown, true);
          return () => window.removeEventListener('keydown', onKeyDown, true);
        }, 'dsh-quick-reload: F5 reload binding');
      },
    };
  },
});
