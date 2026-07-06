export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Serve root "/" as the main HTML file
    if (url.pathname === '/' || url.pathname === '') {
      return env.ASSETS.fetch(
        new Request(new URL('/afterquery-design.html', request.url), request)
      );
    }

    // All other paths (images, etc.) served directly from assets
    return env.ASSETS.fetch(request);
  }
};
