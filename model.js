//订单类
function Order(_order_id,_student_id,_destination,_begin_time,_num){
	var order_id = _order_id;
	var student_id = _student_id;
	var destination = _destination;
	var begin_time = _begin_time;
	var num = _num;
	var time_during = 30 ;
	var isalloted = 0;//是否被分配，初始化为flase
	var iscompleted = 0;//是否完成，初始化为flase
	var waterman_id = "" //送水员id,未分配时为空
	//Order类公有方法（get,set)
  	Order.prototype.get_order_id = function(){
        return order_id;
  	};

  	Order.prototype.set_order_id = function(new_order_id){
           order_id = new_order_id;
  	};

  	Order.prototype.get_student_id = function(){
        return student_id;
  	};

  	Order.prototype.set_student_id = function(new_student_id){
           student_id = new_student_id;
  	};

	Order.prototype.get_destination = function(){
        return destination;
  	};

  	Order.prototype.set_destination = function(new_destination){
           destination = new_destination;
  	};

  	Order.prototype.get_begin_time = function(){
        return begin_time;
  	};

  	Order.prototype.set_begin_time = function(new_begin_time){
           begin_time =new_begin_time;
  	};

    Order.prototype.get_num = function(){
           return num;
  	};

  	Order.prototype.set_num = function(new_num){
           num = new_num;
  	};

  	Order.prototype.get_time_during = function(){
           return time_during;
  	};

  	Order.prototype.set_time_during = function(new_time_during){
          time_during = new_time_during;
  	};

  	Order.prototype.get_isalloted = function(){
           return isalloted;
  	};

  	Order.prototype.set_isalloted = function(new_isalloted){
          isalloted = new_isalloted;
  	};

  	Order.prototype.get_iscompleted = function(){
           return iscompleted;
  	};

  	Order.prototype.set_iscompleted = function(new_iscompleted){
          iscompleted = new_iscompleted;
  	};

  	Order.prototype.get_waterman_id = function(){
           return waterman_id;
  	};

  	Order.prototype.set_waterman_id = function(new_waterman_id){
          waterman_id = new_waterman_id;
  	};


} 


	

  	
//test
var c = new Order(1,1,1,1,1);
alert(c.get_num());


//定义初始的用户类（所用用户及继承此类）
	function User() {
		//私有变量用户的id，密码
　　　　var password ;
        var id ;
        User.prototype.getid = function(){
        	return id;
        };

        User.prototype.setid = function(newid){
            id = newid;
        };

        User.prototype.getpassword = function(){
        	return password;
        };

        User.prototype.setpassword = function(newpassword){
        	password = newpassword;
        }; 
　　}
		
     	  
//User类定义完成


//定义学生类
	function Student(){
	//继承于User类，私有变量为id，password
	
	}
    Student.prototype = new User();
	
	//为学生类添加公有方法
  
  //create 方法
	Student.prototype.create = function(_id,_password){
    Student.prototype = new User();
    this.prototype.setpassword(_password);
    this.prototype.setid(_id);
  }
	//获取订单通过学生ID
	Student.prototype.get_order_by_student_id = function(student_id){
		//通过学生id在服务端请求并查询其相关订单
		var order_list = [];
		//实现代码,从服务端查询
		return order_list;
	};

	//获取订单通过订单ID
	Student.prototype.get_order_by_order_id = function(order_id){
		//通过订单id在服务端请求并查询其相关订单
		var res_order=new Order(0,0,0,0,0);
		//实现代码,从服务端查询
		return res_order;
	};

	//添加订单
	Student.prototype.add_order = function(_order_id,_student_id,_destination,_begin_time,_num){
      var new_order = new Order(_order_id,_student_id,_destination,_begin_time,_num);
      //插入远程数据库
	};

	//确认订单
	Student.prototype.confirm_order = function(order_id){
     var the_order = get_order_by_order_id(order_id);
     the_order.set_iscompleted(1);
	};
	//test
	var tmp_stu =new Student();
  tmp_stu.create(2,3);
	//tmp_stu.setpassword(2);
	alert(tmp_stu.getpassword());
  alert(tmp_stu.getid());


//定义送水工类
  function Waterman(){
  //继承于User类，私有变量为id，password
  
  }
  Waterman.prototype = new User();


//获取订单通过订单ID
  Waterman.prototype.get_order_by_order_id = function(order_id){
    //通过订单id在服务端请求并查询其相关订单
    var res_order=new Order(0,0,0,0,0);
    //实现代码,从服务端查询
    return res_order;
  };


//获取订单通过waterman_id
  Waterman.prototype.get_order_by_waterman_id = function(waterman_id){
    //通过waterman_id在服务端请求并查询其相关订单
    var order_list = [];
    //实现代码,从服务端查询
    return order_list;
  };



//定义Manager类

  function Manager(){
  //继承于User类，私有变量为id，password
  
  }
  Manager.prototype = new User();
  Manager.prototype.create = function(_id,_password){
    setpassword(_password);
    setid(_id);
  }

//获取订单通过订单ID
  Manager.prototype.get_order_by_order_id = function(order_id){
    //通过订单id在服务端请求并查询其相关订单
    var res_order=new Order(0,0,0,0,0);
    //实现代码,从服务端查询
    return res_order;
  };

//获取订单通过waterman_id
  Manager.prototype.get_order_by_waterman_id = function(waterman_id){
    //通过waterman_id在服务端请求并查询其相关订单
    var order_list = [];
    //实现代码,从服务端查询
    return order_list;
  };

//获取订单通过学生ID
  Manager.prototype.get_order_by_student_id = function(student_id){
    //通过学生id在服务端请求并查询其相关订单
    var order_list = [];
    //实现代码,从服务端查询
    return order_list;
  };

//添加订单
  Manager.prototype.add_order = function(_order_id,_student_id,_destination,_begin_time,_num){
      var new_order = new Order(_order_id,_student_id,_destination,_begin_time,_num);
      //插入远程数据库
  };

//删除订单
  Manager.prototype.delete_order = function(_order_id){

  }

//获取当前所有送水工状态
  Manager.prototype.get_waterman_message = function(){

  }

//开启系统
  Manager.prototype.open_system = function(){

  }

//关闭系统
  Manager.prototype.close_system = function(){

  }

//添加公告
  Manager.prototype.notice = function(){

  }

//分配送水工
  Manager.prototype.allot_waterman = function(_order_id,waterman_id){

  }
   