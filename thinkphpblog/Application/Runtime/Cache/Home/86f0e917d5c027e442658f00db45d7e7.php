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
		<h1>文章内容</h1>
<h4><?php echo ($postpage["title"]); ?></h4>
<h5><?php echo (date('Y:m:d H:i:s',$postpage["timestamp"])); ?></h5>
<p><?php echo ($postpage["content"]); ?></p>
	</div>
	<footer>@copyright mtianyan所有</footer>
	
</body>
</html>