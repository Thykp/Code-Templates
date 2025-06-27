package service

import "backend/model"

var users = []model.User{
    {ID: 1, Username: "Alice"},
    {ID: 2, Username: "Bob"},
}

func GetAllUsers() []model.User {
    return users
}

func GetUserByID(id int) *model.User {
    for _, user := range users {
        if user.ID == id {
            return &user
        }
    }
    return nil
}
