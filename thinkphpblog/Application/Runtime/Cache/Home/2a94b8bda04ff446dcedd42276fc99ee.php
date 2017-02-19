<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>我的博客</title>
</head>
<style>
	html,body {
	margin: 0;
	padding: 0;
	}
	header, footer{
		padding: 30px 40px;
		background-color: #f2f2f2;
		color :#666;
	}
	#content{
		padding: 30px 40px;
	}
	header a{
		padding: 0 20px;
		color:  #999;
		text-decoration: none;
	}
	header a:hover{
		color:#333;
	}
	footer{
		text-align: center;
	}
</style>


<body>
	<header>
	<a href="<?php echo U('index/index');?>">首页</a>
	<a href="<?php echo U('index/listpage');?>">文章</a>

	</header>
	<div id="content">
		<h1>欢迎来到我的博客</h1>
<p>其实真正的博客在
<a href="http://www.baidu.com" target="_blank">这里</a>

</p>
<form action="<?php echo U('Index/handle');?>" method="post" >
	<h4>添加文章</h4>
	<input type="text" name="title" placeholder="标题">
	<br>
	<textarea name ="content" cols="30" rows="20" placeholder="内容" ></textarea>
	<button type="submit" >提交</button>
</form>
	</div>
	<footer>@copyright mtianyan所有</footer>
	
</body>
</html>