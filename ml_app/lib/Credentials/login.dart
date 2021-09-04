import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class MyLogin extends StatefulWidget {
  @override
  _MyLoginState createState() => _MyLoginState();
}

class _MyLoginState extends State<MyLogin> {
  var authc = FirebaseAuth.instance;
  late String email;
  late String password;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: SingleChildScrollView(
          child: Center(
            child: Container(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    "Login Page",
                    style: TextStyle(
                        fontSize: 30.0,
                        fontWeight: FontWeight.bold,
                        color: Colors.white),
                  ),
                  SizedBox(
                    height: 15,
                  ),
                  Container(
                      margin: EdgeInsets.only(left: 30, right: 30),
                      width: 400,
                      height: 300,
                      child: Image.asset("assets/robot.gif")),
                  SizedBox(
                    height: 20,
                  ),
                  Container(
                    width: 350,
                    child: TextField(
                      style: TextStyle(color: Colors.white),
                      keyboardType: TextInputType.emailAddress,
                      onChanged: (value) {
                        email = value;
                      },
                      decoration: InputDecoration(
                        hintText: "Enter Email Address",
                        prefixIcon: Icon(Icons.email, color: Colors.white),
                        hintStyle: TextStyle(color: Colors.white),
                        enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                            borderSide:
                                BorderSide(width: 2, color: Colors.lightBlue)),
                        focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                            borderSide:
                                BorderSide(width: 2, color: Colors.lightBlue)),
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 20,
                  ),
                  Container(
                    width: 350,
                    child: TextField(
                      style: TextStyle(color: Colors.white),
                      obscureText: true,
                      onChanged: (value) {
                        password = value;
                      },
                      decoration: InputDecoration(
                        hintText: "Enter Password",
                        prefixIcon: Icon(Icons.lock, color: Colors.white),
                        hintStyle: TextStyle(color: Colors.white),
                        enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                            borderSide:
                                BorderSide(width: 2, color: Colors.lightBlue)),
                        focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                            borderSide:
                                BorderSide(width: 2, color: Colors.lightBlue)),
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 40,
                  ),
                  Material(
                    color: Colors.blue.shade600,
                    borderRadius: BorderRadius.circular(10),
                    elevation: 10,
                    child: MaterialButton(
                      textColor: Colors.white,
                      minWidth: 200,
                      height: 40,
                      child: Text("Login", style: TextStyle(fontSize: 20.0)),
                      onPressed: () async {
                        try {
                          var userSignIn =
                              await authc.signInWithEmailAndPassword(
                                  email: email, password: password);
                          if (userSignIn != null) {
                            Fluttertoast.showToast(
                                msg: "Login Successfully",
                                toastLength: Toast.LENGTH_LONG,
                                gravity: ToastGravity.BOTTOM,
                                timeInSecForIosWeb: 10,
                                backgroundColor: Colors.blue,
                                textColor: Colors.white,
                                fontSize: 16.0);
                            Navigator.pushNamed(context, "ml");
                          }
                        } catch (e) {
                          Fluttertoast.showToast(
                              msg: "Login Failed",
                              toastLength: Toast.LENGTH_LONG,
                              gravity: ToastGravity.BOTTOM,
                              timeInSecForIosWeb: 10,
                              backgroundColor: Colors.blue,
                              textColor: Colors.white,
                              fontSize: 16.0);
                          print(e);
                        }
                      },
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
