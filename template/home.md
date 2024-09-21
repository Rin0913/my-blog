<img id="stamp" class="warning" offset="n" src="/s/top_secret.png">
<img id="stamp" class="warning" offset="y" src="/s/top_secret.png">

# K Rin 的網站

歡迎來到我的網站，可隨意逛逛。


<style>

@keyframes stamp {
	from {
        filter: blur(10px);
		opacity: 0;
        box-shadow: 10px 10px 10px rgba(0, 0, 0, 0);
	}
	to {
        filter: blur(0.7px);
		opacity: 1;
        box-shadow: 0px 0px 0px rgba(0, 0, 0, 1);
	}
}

.warning {
    opacity: 0;
	animation: stamp 0.10s ease-in forwards;
	animation-delay: 1.2s;
    position: absolute;
    width: 12%;
	min-width: 130px;
	transform: var(--offset, rotate( 11deg));
	left: 70%;
	top: 13%;
}

.warning[offset="y"] { --offset: translate(2px, 2px) rotate(13deg) };

</style>
