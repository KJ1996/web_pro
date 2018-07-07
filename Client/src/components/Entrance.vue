<template>
  <div id = "container" class = "container">
	<div id = "form-wrapper">
	  <div id = "imageAside">
		<div id = "imgItSelf"></div>
	  </div>
	  <div id = "form-container">
		<div id = "form-header">
		  <br>
		  <a href="/#/signUp" hidefocus = "true">新用户注册</a>&nbsp | &nbsp
		  <a href="/#/login" hidefocus = "true">账号密码登录</a>
		</div>
		<router-view />
	  </div>
	</div>
  </div>	
</template>

<script>
export default {
	name: 'Entrance'
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

#form-wrapper:after {
	content: "";
	display: block;
	width: 0;
	height: 0;
	clear: both;
}

a {
	color: #999;
	text-decoration: none;
}
a:hover {
	color: black;
	text-decoration: underline;
}

@media screen and (min-width: 1000px) {

  #container {
	width:960px;
	min-height: 372px;
	margin: 60px auto;
  }

  #form-container {
	width: 335px;
	float: right;
	border: 1px solid #a0b1c4;
	border-radius: 5px;
	height: 100%;
  }

  #imageAside {
	position: relative;
	margin-right: 395px;
  }

  #imgItSelf {
	background-image: url(../assets/abc.gif);
	background-position: 170px 75px;
	position: absolute;
	left: 0;
	right: 0;
	top: 0;
	height: 400px;
	background-repeat: no-repeat;
  }

  #form-header {
	height: 50px;
	border-bottom: 1px solid #c0cdd9;
	background-color: #f9fbfe;
	margin-bottom: 25px;
	text-align: center;
  }

}

@media screen and (max-width: 1000px) {
  body {
	background-color: rgb(238,238,238);
  }
  #imageAside {
	display: none;
  }
  #container {
	width:320px;
	min-height: 372px;
	display: flex;
	justify-content: center;
	align-items: stretch;
	margin:0 auto;
  }

  #form-container {
	width: 320px;
	height: 100%;
  }

  #form-header {
	height: 50px;
	border-bottom: 1px solid #c0cdd9;
	margin-bottom: 25px;
	text-align: center;
  }
  
}
</style>
