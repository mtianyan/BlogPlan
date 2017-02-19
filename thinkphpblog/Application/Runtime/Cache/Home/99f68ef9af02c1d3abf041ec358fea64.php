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
		<style type="text/css">
	.p{
		padding: 10px 30px;
		border: 1px solid #888;
		margin: 20px 0;
	}


</style>
<h1>文章列表</h1>
    <div id="listpage">
    	<?php if(is_array($data)): foreach($data as $key=>$v): ?><div class="p">
    		<h4><a href="<?php echo U('Index/postpage',array('id'=>$v['id']));?>"><?php echo ($v["title"]); ?></a></h4>
    		
    		<p><?php echo (date('Y:m:d H:i:s',$v["timestamp"])); ?></p>

    	</div><?php endforeach; endif; ?>
		
</div>

	</div>
	<footer>@copyright mtianyan所有</footer>
	
</body>
</html>