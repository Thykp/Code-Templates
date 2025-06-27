package main

import (
    "backend/router"
    "github.com/cloudwego/hertz/pkg/app/server"
)

func main() {
    h := server.New()
    router.RegisterRoutes(h)
    h.Spin()
}
