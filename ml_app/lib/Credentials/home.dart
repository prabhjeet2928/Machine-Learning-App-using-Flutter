import 'package:flutter/material.dart';

class MyHome extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                  margin: EdgeInsets.only(left: 30, right: 30),
                  width: 400,
                  height: 400,
                  child: Image.asset("assets/ml_brain.gif")),
              SizedBox(
                height: 20,
              ),
              Material(
                color: Colors.lightBlue.shade600,
                borderRadius: BorderRadius.circular(10),
                elevation: 10,
                child: MaterialButton(
                  minWidth: 250,
                  height: 60,
                  textColor: Colors.white,
                  child: Text("Registration", style: TextStyle(fontSize: 20.0)),
                  onPressed: () {
                    Navigator.pushNamed(context, "reg");
                  },
                ),
              ),
              SizedBox(
                height: 25,
              ),
              Material(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
                elevation: 10,
                child: MaterialButton(
                  minWidth: 250,
                  height: 60,
                  textColor: Colors.lightBlue.shade600,
                  child: Text("Login", style: TextStyle(fontSize: 20.0)),
                  onPressed: () {
                    Navigator.pushNamed(context, "login");
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
