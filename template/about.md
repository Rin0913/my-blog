<div class="top-right-text">
    <p>也許……<p>
    <p class="text-padding1">我的誕生就是爲了要與你相遇。<p>
    <p class="text-padding2">——<a class="secret" onclick="openf()">渚薰</a></p>
    <hr />
</div>

<div class="about-main">

# K Rin

你好，我是 K Rin。


目前就讀資訊工程學系，擅長 Python，也會一點 C/C++，目前在研究演算法和作業系統。

喜歡新世紀福音戰士，喜歡旅遊、泡溫泉。歡迎認識哦！

如果要聯繫我：
- [<i class="fa-brands fa-github"></i> Rin0913](https://github.com/Rin0913)
- [<i class="fa-brands fa-telegram"></i> k_rin0913](https://t.me/k_rin0913)
- [<i class="fa-brands fa-facebook"></i> K Rin](https://www.facebook.com/profile.php?id=61565613403764)
- [<i class="fa-solid fa-envelope"></i> contact@sandb0x.tw](mailto:contact@sandb0x.tw)

#### 參考

- [素材來源放 GitHub Repo 的 README](https://github.com/Rin0913/my-blog)

<img class="bottom-right-icon" src="/s/WILLE.png">

</div>

<!-- 以下為一些外部引用以及設定 -->

<style>

.about-main {
    padding-bottom: 5em;
}

.secret {
    color: #333;
}

@font-face {
	font-family: 'GenWanMin2TW';
	src: url('/s/GenWanMin2TW-EL.otf') format('opentype');
}

.top-right-text {
    font-family: "GenWanMin2TW", serif;
    font-weight: 400;
    position: absolute;
    top: 0.5em;
    right: 1em;
    font-size: 22px;
    line-height: 1;
    color: #333;
    padding: 13px 13px;
}

.bottom-right-icon {
    display: inline-block;
    position: absolute;
    bottom: 30px;
    right: 10px;
    min-width: 130px;
    width: 12%;
    opacity: 0.8;
}

.bottom-right-logo {
    display: none;
}

.text-padding1 {
    padding-left: 2em;
}

.text-padding2 {
    padding-left: 9em;
}

.small-img {
    width: 20%;
}

@media (max-width: 1200px) {
    .small-img {
        display: none;
    }
    .about-main {
        padding-top: 10em;
    }
}


</style>

<script>
    var wille = document.querySelectorAll('.bottom-right-icon')[0];
    function openf() {
        // anti-crawler xD
        window.location.href = atob("L2IvJUU4JTk2JUIwJUU1JTkyJThDJUU2JTg4JTkxJUU3JTlBJTg0JUU4JTg3JUFBJUU3JTk5JUJELm1kCg==");
    }
    function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
    async function recolor() {
        let i = 0;
        while(1) {
            wille.style.filter = `hue-rotate(${i}deg)`
            i += 1;
            i %= 360;
            await sleep(1200/i/i/i);
        }
    }
    recolor();
</script>
