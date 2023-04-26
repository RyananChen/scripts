B站跳过片头片尾脚本
===========
[](#油猴脚本链接)油猴脚本链接
-------------
**自动版**:https://greasyfork.org/zh-CN/scripts/463515  
**手动版**:https://greasyfork.org/zh-CN/scripts/463516

[](#项目地址)项目地址
-------------
https://github.com/RyananChen/scripts/tree/main/BiliBili-skip-IntroL-Outro-Tampermonkey

[](#脚本原理)脚本原理
-------------
使用js中**video.currentTime**和**video.duration**的关系来判断时间

[](#配置)配置
-------------

使用脚本**需要设置两个参数**： **片头时长**和**片尾时长**，单位都是秒.   
比如, 片头时长为90秒, 片尾时长为44秒,那么代码前两行为:

```
var skip_IntroLength = 90; // 设置片头长度，单位为秒
var skip_OutroLength = 44; // 设置片尾长度，单位为秒
```

[](#使用方法)使用方法
-------------

把脚本安装进**油猴脚本**内,**填好片头片尾的秒数**即可  
**自动版**:自动执行,两秒钟判断一次是否执行.  
**手动版**:按下CTRL按键或者+=按键即可执行.  

[](#注意事项)注意事项
-------------
固定片头片尾时长,适合看同一部番剧时使用,如果短时间看不同的番剧,容易时间跳多跳少.  
这时建议用白名单和黑名单功能,复制几份代码出来生成不同脚本,给不同名字,给不同片头片尾时长.  
一个油猴脚本对应一个番即可,设置一次之后都省力.
```
黑名单
// @exclude      https://example.com/*
白名单
// @match        https://example.com/*
星号*表示正则的匹配.
```


[](#自动版脚本)自动版脚本
---------

``` js
// ==UserScript==
// @name         B站哔哩哔哩bilibili跳过番剧片头片尾【自动版】
// @description  bilibili B站自动跳过番剧片头片尾。可在代码第一行第二行修改片头和片尾时间。支持edge以及chrome。项目地址https://github.com/RyananChen/scripts/tree/main/BiliBili-skip-IntroL-Outro-Tampermonkey
// @namespace    http://tampermonkey.net/
// @version      1.2
// @author       RyananChen
// @match        https://www.bilibili.com/bangumi/play/*
// @license      BSD
// @grant        none
// ==/UserScript==
/*
//此脚本作用域match只作用于番剧，避免其他视频也触发快捷键。如果改作用域到b站全部可以写@match        https://www.bilibili.com/video/*
//但这么做会导致看什么视频都跳过，不合适。
//参考链接
chatgpt
https://greasyfork.org/zh-CN/scripts/443560
https://greasyfork.org/zh-CN/scripts/441461
*/

const skip_IntroLength = 90; // 设置片头长度，单位为秒
const skip_OutroLength = 44; // 设置片尾长度，单位为秒

(function()
{
	setInterval(() =>
	{
		const video = document.querySelector("#bilibili-player video"); // 获取页面上的视频元素
		if (video && !isNaN(video.duration)) //如果获取到视频元素并且视频总长度为数字还是啥，没细看isnan。
		{
			const currentTime = video.currentTime; // 获取当前播放时间的时间戳
			if (currentTime < skip_IntroLength)
			{
				video.currentTime = skip_IntroLength; // 如果仍处于片头时间，将视频进度设置为90秒
			}
			//如果当前播放时间大于【视频总长度-片尾曲时间】，并且小于【视频总长度-2秒】
			//则跳到【视频总长度】，加了那个并且的条件是为了防止它一直重复跳导致卡顿。
			else if (currentTime > (video.duration - skip_OutroLength) && currentTime < (video.duration - 2))
			{ //duration 属性返回当前视频的长度，以秒计算。
				video.currentTime = video.duration; // 如果处于片尾时间，将视频进度设置为结束
				/*
				原本想在片尾的时候停止脚本几秒钟，来防止脚本循环操作。
				后来通过在else if的条件中加上了&& currentTime < (video.duration - 2)来避免了这个情况的发生。
				并且这个等待不生效啊。具体没看，再议。
				setTimeout(() => {
				    // 等待15秒后进行后续操作
				    // 这里可以放置需要执行的代码
				    console.log('15秒已过，可以进行后续操作了');
				}, 15000);
				*/
			}
		}
	}, 2000); // 每2秒执行一次setInterval，检查一次视频播放进度
})();
```

[](#手动版脚本)手动版脚本
---------
``` js 
// ==UserScript==
// @name         B站哔哩哔哩bilibili跳过番剧片头片尾【手动版】
// @description  在b站番剧页面，按下  =+键  或者  ctrl键  后，跳过片头曲或片尾曲。可在配置文件修改片头片尾时间。项目地址https://github.com/RyananChen/scripts/tree/main/BiliBili-skip-IntroL-Outro-Tampermonkey
// @namespace    http://tampermonkey.net/
// @version      1.0
// @author       RyananChen
// @match        https://www.bilibili.com/bangumi/play/*
// @license      BSD
// @grant        none
// ==/UserScript==
/*
//此脚本作用域match只作用于番剧，避免其他视频也触发快捷键。如果改作用域到b站全部可以写@match        https://www.bilibili.com/video/*
//但这么做会导致看什么视频都跳过，不合适。
//参考链接
chatgpt
https://greasyfork.org/zh-CN/scripts/443560
https://greasyfork.org/zh-CN/scripts/441461
*/
var skip_IntroLength = 90; //片头曲时间||需要跳过的时间，请把这一项设置为你要跳过的片头时长。
var skip_OutroLength = 44; // 设置片尾长度，单位为秒
var waitTime = 6; //等待时间，用于跳过片尾之后切换到下一集的等待，根据网络情况调整。


//ryan:等待函数，请注意，您需要在async函数中使用await关键字才能等待wait函数完成。
//如果您尝试在非异步函数中使用await，将会得到一个语法错误。：
function wait(time)
{
	return new Promise(resolve => setTimeout(resolve, time));
}

//主函数，给function加了一个async
document.addEventListener('keyup', async function(e)
{
	if (e.keyCode === 187 || e.keyCode === 17)
	{ //187代表“=+”的keycode值，17代表ctrl的keycode值。keycode值可在https://www.cnblogs.com/lxwphp/p/9548823.html查询
		var video = document.querySelector("#bilibili-player video");
		const currentTime = video.currentTime; // 获取当前播放时间的时间戳
		//如果当前播放时间在片头，就跳到片头曲结束。
		if (currentTime < skip_IntroLength)
		{
			video.currentTime = skip_IntroLength; // 如果仍处于片头时间，将视频进度设置为90秒
		}
		//如果当前播放时间在片尾，就跳到片头曲结束，等待几秒钟到下一集。然后再跳到下一集的片头曲结束。
		else if (currentTime > (video.duration - skip_OutroLength) &&currentTime < (video.duration - 2)) //duration 属性返回当前视频的长度，以秒计算。
		{
			video.currentTime = video.duration;
			await wait(waitTime * 1000);//等待生效了，没问题。
			//这里必须要再次获取一次currentTime，因为切换集数了，不获取的话此时的currentTime值是不太对的，无法执行下面的跳转操作
			const currentTime = video.currentTime;
			video.currentTime = skip_IntroLength;
		}
	}
})

/*
        //原本的手动版本快进代码如下：思路是按下按键之后，跳过片头曲的时间，那么会出现两种情况
        //1.
        //在片头，此时先跳到了video.currentTime+skip_IntroLength-waitTime的时间，大概是片头曲结束的前几秒。
        //跳过去之后等待waitTime秒钟，再次跳转到skip_IntroLength，即片头曲结束刚刚好的时间。
        //2.
        //在片尾，此时因为已经播放了，currentTime接近结束了，加上片头曲的时间之后，会跳到视频结束。
        //然后等待waitTime秒钟，就会换到下一个视频。此时再执行跳转到skip_IntroLength，就会跳到下一个视频的片头曲结束。
        //逻辑问题：
        //原本逻辑是挺好的，但是如果大家都用的话，手动版的问题在于，如果片尾曲比片头曲长
        //就无法跳过片尾曲，还会在想跳过片尾曲的时候，跳到本集的片头曲结束时间点，即1：30。
        //所以弃用这个逻辑，用自动版的逻辑，代码保留其他人参考用。
function wait(time)
{
	return new Promise(resolve => setTimeout(resolve, time));
}
document.addEventListener('keyup', async function(e)
{
	if (e.keyCode === 187 || e.keyCode === 17) //187代表“=+”的keycode值，17代表ctrl的keycode值。keycode值可在https://www.cnblogs.com/lxwphp/p/9548823.html查询
	{
		var video = document.querySelector('video');
		video.currentTime = video.currentTime + skip_IntroLength - waitTime; //此处设置快进时间，单位秒
		video.muted = true; //静音，免得时间不对有声音重复比较烦。
		await wait(waitTime * 1000); //等待waitTime秒钟，此处单位毫秒ms
		video.currentTime = skip_IntroLength; //此处设置跳转时间，单位秒
		video.muted = false; //解除静音
	}
})
        */
```
