package main

import (
	"fmt"
)

func main() {
	arr := []interface{}{
		1, []interface{}{
			2, []interface{}{3,
				[]interface{}{4},
			}, 5,
		},
	}
	res := flattenArray(arr)
	fmt.Println(res)
}

func flattenArray(arr []interface{}) []int {
	var res []int
	for _, v := range arr {
		if val, ok := v.(int); ok {
			res = append(res, val)
		} else if value, ok := v.([]interface{}); ok {
			for _, val := range flattenArray(value) {
				res = append(res, val)
			}
		}
	}
	return res
}
