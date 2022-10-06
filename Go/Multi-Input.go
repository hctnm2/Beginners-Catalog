package main
import "fmt"

func main() {
  var n,
  k,
  j,
  l,
  m,
  v int
  fmt.Scanln(&n)
  fmt.Scanln(&k)
  fmt.Scanln(&j)
  fmt.Scanln(&l)
  fmt.Scanln(&m)
  fmt.Scanln(&v)
  a: = make([]int, n)
  cc: = a[n: n]
  if v != 0 {
    cc = append(cc, k, j, l, m, v)
  } else {
    cc = append(cc, k, j, l, m)
  }
  fmt.Println(cc)
}
