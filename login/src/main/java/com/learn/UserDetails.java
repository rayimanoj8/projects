package com.learn;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;

@Entity
public class UserDetails {
    
    @Id
    private int id;
    private String name;
    private String email;
    
    @OneToOne(mappedBy = "user")
    private UserCredentials credentials;
    
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email.toLowerCase();
    }
    public void setEmail(String email) {
        this.email = email.toLowerCase();
    }
    @Override
    public String toString() {
        return "UserDetails [id=" + id + ", name=" + name + ", email=" + email + "]";
    }
}