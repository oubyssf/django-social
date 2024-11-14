(function(){
    if(!window.bookmarklet) {
        let bookmarklet_js = document.body.
            appendChild(
                document.createElement('script')
            );
        let url = '//127.0.0.1:8000/static/js/bookmarklet.js?r=';
        let rand = Math.floor(Math.random()*99999999999999);
        bookmarklet_js.src = url + rand;
        window.bookmarklet = true;
    } else {
        bookmarkletLaunch();
    }
})();