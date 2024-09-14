"use strict";

function wsPlayer(videoId, wsUrl) {
    this.videoId = videoId;
    this.wsUrl = wsUrl;
    this.ws = null;
    this.frameQueue = [];
    console.log("wsPlayer v1.0.1 20220423");
}

wsPlayer.prototype.open = function () {
    let sourcebuffer = null;
    this.ws = new WebSocket(this.wsUrl);
    this.ws.binaryType = 'arraybuffer';
    let firstMessage = true;
    
    let demux_moov = function (info) {
        let codecs = [];
        for (let i = 0; i < info.tracks.length; i++) {
            codecs.push(info.tracks[i].codec);
        }
        console.log(codecs);
        let video = document.getElementById(this.videoId);
        let mediasource = new MediaSource();
        video.src = URL.createObjectURL(mediasource);
        let pre_pos = 0;
        mediasource.onsourceopen = function() {
            sourcebuffer = mediasource.addSourceBuffer('video/mp4; codecs="' + codecs.join(', ') + '"');
            sourcebuffer.onupdateend = function() {
                let pos = video.currentTime;
                if(video.buffered.length > 0) {
                    let start = video.buffered.start(video.buffered.length - 1);
                    let end = video.buffered.end(video.buffered.length - 1);
                    //console.log("pos=" + pos + ",start=" + start + ",end=" + end);

                    if (pos < start) {
                        //console.log("set video.currentTime pos=" + pos + ",start=" + start + ",end=" + end);
                        video.currentTime = start;
                    }

                    if(pos > end) {
                        //console.warn("chase frame pos=" + pos + ",start=" + start + ",end=" + end);
                        video.currentTime = start;
                    }

                    if (pos - pre_pos != 0 && end - pos > 3) {
                        //console.log("set end video.currentTime pos=" + pos + ",start=" + start + ",end=" + end);
                        video.currentTime = end;
                    }

                    for (let i = 0; i < video.buffered.length - 1; i++) {
                        let prestart = video.buffered.start(i);
                        let preend = video.buffered.end(i);
                        if(!sourcebuffer.updating) {
                            sourcebuffer.remove(prestart, preend);
                        }
                    }

                    if(pos - start > 10 && !sourcebuffer.updating) {
                        //console.warn("remove start pos=" + pos + ",start=" + start + ",end=" + end);
                        sourcebuffer.remove(0, pos - 3);
                    }

                    if(end - pos > 10 && !sourcebuffer.updating) {
                        //console.warn("remove end pos=" + pos + ",start=" + start + ",end=" + end);
                        sourcebuffer.remove(0, end - 3);
                    }
                }
                pre_pos = pos;
            }
        }
    }.bind(this);

    this.ws.onmessage = function(e) {
        if(firstMessage) {
            firstMessage = false;
            let moov = e.data;
            let mp4Box = new MP4Box;
            mp4Box.onReady = demux_moov;
            moov.fileStart = 0;
            mp4Box.appendBuffer(moov);
        }
        this.frameQueue.push(e.data);
        if (!sourcebuffer || sourcebuffer.updating) {
            return;
        }
        if(this.frameQueue.length === 1) {
            try {
                sourcebuffer.appendBuffer(this.frameQueue.shift());
            }catch (e) {
                console.log("ourcebuffer.appendBuffer(this.frameQueue.shift())",e)
            }

        } else {
            let byte_length = 0;
            for (const qnode of this.frameQueue) {
                byte_length += qnode.byteLength;
            }
            let mp4buf = new Uint8Array(byte_length);
            let offset = 0;
            for (const qnode of this.frameQueue) {
                let frame = new Uint8Array(qnode);
                mp4buf.set(frame, offset);
                offset += qnode.byteLength;
            }
            sourcebuffer.appendBuffer(mp4buf);
            this.frameQueue.splice(0, this.frameQueue.length);
        }
    }.bind(this);
}

wsPlayer.prototype.close = function () {
    this.ws && this.ws.close();
}