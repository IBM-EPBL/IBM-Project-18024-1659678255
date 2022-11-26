<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>

    <title>Nutrition Assistant</title>
    <link rel="icon" href="{{ url_for( 'static', filename = 'src/cardiogram.png')}}">
    <link rel="stylesheet" href="{{ url_for( 'static', filename = 'css/index.css')}}">
    <style>

    </style>
</head>
<body>
    {% if error %}
        <p style="font-size:20px;padding:20px;background-color:red;border-radius:20px;margin: 10px 40px">{{error}}</p>
    {% endif %}


    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-5 colh heading">
          <p class="display-3">Nutrition Assistant</p>
        </div>
        <div class="col-lg-7 colh">
          <div>
            <ul class="lists">
              <li> <a id="c1" href="#cont_1">Home</a></li>
              <li onmouseover = "signinOne(this)" onmouseout="unsignin(this)"> <a id="c2" href="#logins">SignIn</a></li>
              <li onmouseover = "signinTwo(this)" onmouseout="unsignin(this)"> <a id="c3" href="#logins">SignUp</a></li>
              <li onmouseover = "visible(this)" onmouseout="unsignin(this)"> <a id="c4" href="#abouts">About</a></li>
            </ul>
          </div>        
        </div>
      </div>
    </div>

    <div class="container-fluid content">
      <div class="row">
        <div class="col-lg info">
            <p>
              Nutritional support is the provision of adequate nutrients to maintain a 
              healthy body weight and avoid malnutrition. The continuous delivery of 
              high-quality and cost-effective nutritional care to patients has been 
              shown to be an increasingly difficult task. It is observed that dieticians 
              are requested to carry out the nutritional assessment, to manually 
              calculate the nutritional needs and to design the everyday meal plan for 
              each patient. In most cases, these time-consuming tasks are not completed 
              due to lack of time or inadequate number of personnel. Development of a 
              computer assisted information tool with cloud-based on-line diet 
              consultation module and comparison of its efficacy with one- to-one 
              counselling would be efficiently utilized for client education intervention 
              programs. The nutrient content calculation was planned to undertake with 
              commonly consumed traditional as well as junk foods
            </p>
        </div>
        <div class="col-lg info" id="infos">
          <div class="cont_1 pb-0">
            <div onclick="ont()" id="l1" class="options">
              <p><img src="{{ url_for( 'static', filename = 'src/home.png')}}" width="60" height="60" alt=""><p class="list">Home</p>
            </div>
            <div id="l2" class="options">
              <p><img src="{{ url_for( 'static', filename = 'src/login.png')}}" width="60" height="60" alt=""><p class="list">Sign In</p>
            </div>
            <div id="l3" class="options">
              <p><img src="{{ url_for( 'static', filename = 'src/sign-up.png')}}" width="60" height="60" alt=""><p class="list">Sign Up</p>
            </div>
            <div id="l4" class="options">
              <p><img src="{{ url_for( 'static', filename = 'src/info.png')}}" width="60" height="60" alt=""><p class="list">about</p>
            </div>

          <div id="logins" class="login">
            <div class="container" id="container">
              <div class="form-container sign-up-container">
                <form action="{{ url_for('register') }}" method="post" enctype="multipart/form-data">
                <h1>Create Account</h1>
                
                <input type="text" name="name" placeholder="Name" required />
                <input type="email" name="email" placeholder="Email" required />
                <input type="password" name="pass" placeholder="Password" required />
                <button>Sign Up</button>
                </form>
              </div>
              <div class="form-container sign-in-container">
                <form action="{{ url_for('homepage') }}" method="post" enctype="multipart/form-data">
                <h1>Sign in</h1>
                  <input STYLE="display:none" type="text" name="name" placeholder="Name"/>
                  <input type="email" name="email" placeholder="Email" required />
                  <input type="password" name="pass" placeholder="Password" required />
                  <a href="{{url_for('forgot')}}">Forgot your password?</a>
                <button>Sign In</button>
                </form>
              </div>
              <div class="overlay-container">
                <div class="overlay">
                <div class="overlay-panel overlay-left">
                  <h1>Welcome Back!</h1>
                  <p>To keep connected with us please login with your personal info</p>
                  <button class="ghost" id="signIn">Sign In</button>
                </div>
                <div class="overlay-panel overlay-right">
                  <h1>Hello, Friend!</h1>
                  <p>Enter your personal details and start journey with us</p>
                  <button class="ghost" id="signUp">Sign Up</button>
                </div>
                </div>
              </div>
              </div>
          </div>
          <div class="about" id="abouts">
            <p>
              A web based tool is being planned for therapeutic nutrition prescriptions in clinical settings.
              The cloud based system would have the ability to calculate the nutritional requirements and to
              guide first  line  nutritional  management  to  patients  and  clients  automatically.
            </p>
          </div>
          </div>
        </div>
      </div>
    </div>

</body>
<script src="{{ url_for('static', filename='js/index.js') }}">

  function ont() {
    document.getElementById('info').style.color = 'red';
  }
</script>
</html>
