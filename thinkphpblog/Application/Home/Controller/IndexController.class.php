<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
        $this->display();
    }
    public function listpage()
    {
    	parent::__construct();
    	$data = M('mtianyan');
    	$this->data =$data->select();
    	$this->display();		
    }
    public function handle()
    {
    	$title = I('title');
    	$content = I('content');
    	M('mtianyan')->data(array(
    			'titile' => $title,
    			'content' => $content,
    			'timestamp' => time()
    			))->add();
    	$this -> redirect('Index/listpage');
    }
    public function postpage(){
        $post_id = I('id');
        // echo $post_id;
        $postpage =M('mtianyan')->where(array('id' => $post_id))->find();
        $this->postpage =$postpage;
        $this->display();




    }

}