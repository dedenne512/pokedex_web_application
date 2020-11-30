window.onload = () => {
    var cameraFacing = false;

    const video = document.getElementById("video");
    const canvas = document.querySelector("#picture");
    const se = document.querySelector('#se');
    const cancel = document.querySelector('#cancel');
    
    var w = video.clientWidth;
    var h = video.clientHeight;

    // canvas.setAttribute('width', w);
    // canvas.setAttribute('height', h);

    var mode = cameraFacing ? 'environment' : 'user';

    var medias = {
        audio: false,
        video: {
            facingMode: mode
        }
    };


    // シャッタークリック後ストリームに戻る処理
    cancel.addEventListener('click', e => {
        canvas.classList.add('d-none');
        video.play();
    });  

    // clickイベントリスナーで、切り替えボタンがタップされた時に切り替えを行う。
    change_btn.addEventListener('click', (e) => {
        e.preventDefault();

        cameraFacing = !cameraFacing;


        mode = cameraFacing ? 'environment' : 'user';

        medias.video.facingMode = mode;

        // medias = {
        //     audio: false,
        //     video: {
        //         facingMode: mode
        //     }
        // };

        // フロントカメラをそのまま使うと、左右反転してしまうので、activeクラスとcssでミラー処理
        cameraFacing ? document.querySelector('video').classList.remove("active") : document.querySelector('video').classList.add("active");
        // // canvasはAR.jsを使っている時
        // cameraFacing ? document.querySelector('canvas').classList.remove("active") : document.querySelector('canvas').classList.add("active");

        // Android Chromeでは、セッションを一時停止しないとエラーが出ることがある
        stopStreamedVideo(video);

        // カメラ切り替え
        navigator.mediaDevices.getUserMedia(medias)
            .then(stream => video.srcObject = stream)
            .catch(err => alert(`${err.name} ${err.message}`));

        document.querySelector('#shutter').addEventListener('click', () => {
            const ctx = canvas.getContext('2d');

            // 演出的な目的で一度映像を止めてSEを再生する
            video.pause();  // 映像を停止
            se.play();      // シャッター音
            // setTimeout(() => {
            //     video.play();    // 0.5秒後にカメラ再開
            // }, 500);

            // canvasに画像を貼り付ける
            // ctx.drawImage(video, 0, 0, w, h);
        });
    });

    // // clickイベントリスナーで、切り替えボタンがタップされた時に切り替えを行う。
    // change_btn.addEventListener('click', (e) => {
    //     e.preventDefault();

    //     const video = document.getElementById("video");
    //     const mode = cameraFacing ? 'environment' : 'user';

    //     // フロントカメラをそのまま使うと、左右反転してしまうので、activeクラスとcssでミラー処理
    //     cameraFacing ? document.querySelector('video').classList.remove("active") : document.querySelector('video').classList.add("active");
    //     // // canvasはAR.jsを使っている時
    //     // cameraFacing ? document.querySelector('canvas').classList.remove("active") : document.querySelector('canvas').classList.add("active");

    //     // Android Chromeでは、セッションを一時停止しないとエラーが出ることがある
    //     stopStreamedVideo(video);

    //     // カメラ切り替え
    //     navigator.mediaDevices.getUserMedia({ video: { facingMode: mode } })
    //         .then(stream => video.srcObject = stream)
    //         .catch(err => alert(`${err.name} ${err.message}`));

    //     cameraFacing = !cameraFacing;
    // });

    // videoセッション一時停止
    function stopStreamedVideo(videoElem) {
        let stream = videoElem.srcObject;
        let tracks = stream.getTracks();

        tracks.forEach(function (track) {
            track.stop();
        });

        videoElem.srcObject = null;
    }


    // カメラ切り替え
    navigator.mediaDevices.getUserMedia(medias)
        .then((stream) => {
            video.srcObject = stream;
            video.onloadedmetadata = (e) => {
                video.play();
            };
        })
        .catch(err => alert(`${err.name} ${err.message}`));


    document.querySelector('#shutter').addEventListener('click', () => {
        const ctx = canvas.getContext('2d');

        canvas.classList.toggle('d-none');

        // 演出的な目的で一度映像を止めてSEを再生する
        video.pause();  // 映像を停止
        se.play();      // シャッター音
        // setTimeout(() => {
        //     video.play();    // 0.5秒後にカメラ再開
        // }, 500);

        const wrap = document.querySelector('#wrap');
        wrap.setAttribute('overflow', 'hidden');
        wrap.setAttribute('width', w);
        wrap.setAttribute('height', h);

        // canvasに画像を貼り付ける
        canvas.setAttribute('width', w);
        canvas.setAttribute('height', h);
        video.setAttribute('width', w);
        video.setAttribute('height', h);
        canvas.setAttribute('max-height', h);
        ctx.drawImage(video, 0, 0, w, h);

        // 画像に変換する処理
        canvas.toBlob(blob => {
            var newImg = document.createElement('img'),
                url = URL.createObjectURL(blob);

            newImg.onload = () => {
                URL.revokeObjectURL(url);
            };

            newImg.src = url;
            canvas.appendChild(newImg);
        }, 'image/jpeg', 0.95);
    });
};