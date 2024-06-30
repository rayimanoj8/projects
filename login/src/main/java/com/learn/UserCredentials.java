package com.learn;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.JoinColumn;

@Entity
public class UserCredentials {
    
    @Id
    private String username;
    private String password;

    @OneToOne
    @JoinColumn(name = "user_id")
    private UserDetails user;
    
    public UserDetails getUser() {
        return user;
    }
    public void setUser(UserDetails user) {
        this.user = user;
    }
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    @Override
    public String toString() {
        return "UserCredentials [user=" + user + ", username=" + username + ", password=" + password + "]";
    }
    
}
