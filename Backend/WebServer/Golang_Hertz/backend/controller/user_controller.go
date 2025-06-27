package controller

import (
	"strconv"

	"context"
	"backend/service"

	"github.com/cloudwego/hertz/pkg/app"
	"github.com/cloudwego/hertz/pkg/protocol/consts"
)

func GetAllUsers(c context.Context, ctx *app.RequestContext) {
	users := service.GetAllUsers()
	ctx.JSON(consts.StatusOK, users)
}

func GetUserByID(c context.Context, ctx *app.RequestContext) {
	idStr := ctx.Param("id")
	id, err := strconv.Atoi(idStr)
	if err != nil {
		ctx.JSON(consts.StatusBadRequest, map[string]string{"error": "Invalid ID"})
		return
	}

	user := service.GetUserByID(id)
	if user == nil {
		ctx.JSON(consts.StatusNotFound, map[string]string{"error": "User not found"})
		return
	}

	ctx.JSON(consts.StatusOK, user)
}
