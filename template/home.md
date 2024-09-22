<img class="warning" src="/s/top_secret.png">
<img class="warning" src="/s/top_secret.png">

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
    width: 14%;
	min-width: 130px;
	left: 70%;
	top: 37%;
}


</style>

<script>
	let base = window.screen.width / 10;
	let randint1 = Math.floor(Math.random() * base) - base / 2; 
	let randint2 = Math.floor(Math.random() * base) - base / 2; 
	let randint3 = Math.floor(Math.random() * 41) - 20;
    const stamps = document.querySelectorAll('.warning');
	stamps.forEach(stamp => {
		const stampStyle = window.getComputedStyle(stamp);
		let stampTop = parseInt(stampStyle.top);
		let stampLeft = parseInt(stampStyle.left);
		stamp.style.top = (stampTop + randint1) + 'px';
		stamp.style.left = (stampLeft + randint2) + 'px';
		stamp.style.transform = `rotate(${randint3}deg)`;
		randint3 += 1 + Math.round(Math.random() * 2);
		
	});
</script>
