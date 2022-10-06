package main

import "fmt"

func main() {
  //Define string, int and set result int
  var operator string
  var n1,
  n2 int
  ans: = 0
  //Intial inputs separated by a space on one line
  fmt.Print("Enter 1st Number, operator, 2nd number on same line\n")
  fmt.Scanln(&n1, &operator, &n2)
  //Basic switch operator
  switch operator {
    case "+":
      ans = n1 + n2
      break
    case "-":
      ans = n1 - n2
      break
    case "*":
      ans = n1 * n2
      break
    case "/":
      ans = n1 / n2
      break
    case "%":
      ans = n1 % n2
      break
    default:
      //Operators are only defined as basic + - * / %, not string worded as add sub mul div
      fmt.Println("Invalid Operation")
      break
  }
  //Simple output
  fmt.Printf("%d %s %d = %d", n1, operator, n2, ans)
}
