package com.learn;


import java.util.Scanner;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;


public class App {
    static Scanner sc = new Scanner(System.in);

    static UserDetails createUser() {

        UserDetails user = new UserDetails();
        System.out.println("Enter Your Email :");
        user.setEmail(sc.nextLine());

        System.out.println("Enter Your Id :");
        user.setId(sc.nextInt());
        sc.nextLine();

        System.out.println("Enter Your Name :");
        user.setName(sc.nextLine());

        return user;
    }

    static UserCredentials createUserCredentials(UserDetails user) {
        UserCredentials uc = new UserCredentials();
        uc.setUser(user);
        System.out.println("Enter Your username :");
        uc.setUsername(sc.nextLine());

        System.out.println("Enter Your password :");
        uc.setPassword(sc.nextLine());

        return uc;
    }
    static UserDetails update(UserDetails user){
        System.out.println("Enter Your New Email :");
        user.setEmail(sc.nextLine());

        System.out.println("Enter Your New Name :");
        user.setName(sc.nextLine());

        return user;
    }
    public static void main(String[] args){

        Configuration con = new Configuration()
                .configure()
                .addAnnotatedClass(UserDetails.class)
                .addAnnotatedClass(UserCredentials.class);
        SessionFactory sf = con.buildSessionFactory();
        Session s = sf.openSession();
        Transaction tx = s.beginTransaction();
        System.out.println("Welcome to Hibernate Credentials saver");
        
        System.out.println("Enter Your Choice : ");
        System.out.println("1 . Create User");
        System.out.println("2. Login and Update ");
        System.out.println("Any Other Key To Stop Execution");
        UserDetails main_user = null;
        while(true){
            int choice = sc.nextInt();
            sc.nextLine();
            if (choice == 1 && main_user == null) {
                // user Creation
                UserDetails user = createUser();
                UserCredentials uc = createUserCredentials(user);

                s.save(user);
                s.save(uc);
                tx.commit();

            } else if (main_user!=null || choice == 2) {
                // Login
                if(main_user == null){
                    System.out.println("Welcome User ");
                    System.out.println("Enter Your username :");
                    String username = sc.nextLine();
                    System.out.println("Enter Your password :");
                    String password = sc.nextLine();

                    UserCredentials uc = s.get(UserCredentials.class, username);
                    if(uc.getPassword().equals(password)){
                        main_user = uc.getUser();
                        System.out.println("Your Details Are : " + main_user);
                        System.out.println();
                        System.out.println("Enter 1 For update or Anything Else to LogOut : ");
                        int check = sc.nextInt();
                        sc.nextLine();
                        if(check == 1){
                            // Update Your Details
                            main_user = update(main_user);
                            s.save(main_user);
                            tx.commit();
                            System.out.println("Updates are Succesfull ...");
                        }else{
                            // LogOut
                            System.out.println("Your are Being LogOut ... ");
                            main_user = null;
                        }
                    }else{
                        System.out.println("Try Again... ");
                    }
                }else{
                        System.out.println("Your Details Are : " + main_user);
                        System.out.println();
                        System.out.println("Enter 1 For update or Anything Else to LogOut : ");
                        int check = sc.nextInt();
                        sc.nextLine();
                        if(check == 1){
                            // Update Your Details
                            main_user = update(main_user);
                            s.save(main_user);
                            tx.commit();
                            System.out.println("Updates are Succesfull ...");
                        }else{
                            // LogOut
                            System.out.println("Your are Being LogOut ... ");
                            main_user = null;
                        }
                }
            } else{
                break;
            }
        }

        s.close();
        System.out.println("Thank You FOr Using Our App ...");
    }
}
