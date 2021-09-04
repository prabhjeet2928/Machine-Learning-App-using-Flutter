import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class MyReg extends StatefulWidget {
  @override
  _MyRegState createState() => _MyRegState();
}

class _MyRegState extends State<MyReg> {
  late String email;
  late String password;
  var authc = FirebaseAuth.instance;
  var msgtextemail = TextEditingController();
  var msgtextpassword = TextEditingController();
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
                    "Registration Page",
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
                      controller: msgtextemail,
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
                      controller: msgtextpassword,
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
                        onPressed: () async {
                          msgtextemail.clear();
                          msgtextpassword.clear();
                          try {
                            var user =
                                await authc.createUserWithEmailAndPassword(
                                    email: email, password: password);
                            if (user.additionalUserInfo!.isNewUser == true) {
                              Fluttertoast.showToast(
                                  msg: "Registration Successfully",
                                  toastLength: Toast.LENGTH_LONG,
                                  gravity: ToastGravity.BOTTOM,
                                  timeInSecForIosWeb: 10,
                                  backgroundColor: Colors.lightBlue,
                                  textColor: Colors.white,
                                  fontSize: 16.0);
                              Navigator.pushNamed(context, "ml");
                            }
                          } catch (e) {
                            Fluttertoast.showToast(
                                msg: "Already Registered",
                                toastLength: Toast.LENGTH_LONG,
                                gravity: ToastGravity.BOTTOM,
                                timeInSecForIosWeb: 10,
                                backgroundColor: Colors.lightBlue,
                                textColor: Colors.white,
                                fontSize: 16.0);
                            print(e);
                          }
                        },
                        minWidth: 200,
                        height: 40,
                        child:
                            Text("Register", style: TextStyle(fontSize: 20.0))),
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
