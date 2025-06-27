package router

import (
    "github.com/cloudwego/hertz/pkg/app/server"
    "backend/controller"
)

func RegisterRoutes(h *server.Hertz) {
    userGroup := h.Group("/api/users")
    userGroup.GET("/", controller.GetAllUsers)
    userGroup.GET("/:id", controller.GetUserByID)
}
