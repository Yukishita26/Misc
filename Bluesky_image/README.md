# Bluesky の縦長い画像を小さくする

Bluesky の画像は[横幅の約3倍くらいまでトリミングされずに表示されるらしい](https://bsky.app/profile/ajalaca.bsky.social/post/3kl2bdtk6hk2v) [2024-02-12 現在]．
タイムラインをスクロールして見るにはちょっと見づらいので1:1くらいの領域に収まってくれるようにUIを弄る．

やっつけなので公式がちゃんと対応してくれるまでの対処療法．
雑にフィルターしているので投稿画像以外のものも変わってしまっているかも．

適当なブックマークを作って，URL欄を↓の改行を消したもので置き換える．
ブックマークボタンを押すと画像が縦が横の1/2の長方形の領域に押し込むようになる．
もう一度押すと元に戻す（元のアスペクト比を復元するのが面倒なので一度変更された投稿はそのまま）．

```js
javascript:var cII;c=function(){[...document.querySelectorAll("img")].filter(d=>d.parentNode.className==="").map(d=>{d.parentNode.parentNode.style.aspectRatio=""+Math.max(parseInt(d.parentNode.parentNode.style.aspectRatio.replace(" / 1", "")), 2);d.style.objectFit="contain";});};r=function(){[...document.querySelectorAll("img")].filter(d=>d.parentNode.className==="").map(d=>{d.style.objectFit="cover";});};if(cII){clearInterval(cII);cII=null;r();}else{cII=setInterval(c,500);}
```

改行あり版．
9行目の r=2 は変更する画像領域のアスペクト比．
下から2行目の t=500 は変更処理を行う時間間隔．

```js
javascript:
var cII;
c=function(){
    [...document.querySelectorAll("img")]
        .filter(d=>d.parentNode.className==="")
        .map(d=>{
            d.parentNode.parentNode.style.aspectRatio=""+Math.max(
                parseInt(d.parentNode.parentNode.style.aspectRatio.replace(" / 1", "")),
                2);
            d.style.objectFit="contain";
        });
};
r=function(){
    [...document.querySelectorAll("img")]
        .filter(d=>d.parentNode.className==="")
        .map(d=>{
            d.style.objectFit="cover";
        });
};
if(cII){
    clearInterval(cII);
    cII=null;
    r();
}else{
    cII=setInterval(c,500);
}
```