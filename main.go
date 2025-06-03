package main

import (
	"html/template"
	"log"
	"net/http"
)

var (
	main_template        = template.Must(template.ParseFiles("templates/main.tmpl"))
	mother_info_template = template.Must(template.ParseFiles("templates/motherinfo.tmpl"))
	dad_info_template    = template.Must(template.ParseFiles("templates/dadinfo.tmpl"))
	child_info_template  = template.Must(template.ParseFiles("templates/childinfo.tmpl"))
	visit_info_template  = template.Must(template.ParseFiles("templates/visitinfo.tmpl"))
)

type IndexData struct {
	Name string
}

type MotherInfo struct {
	Name        string
	NationalId  string
	PhoneNumber string
}

func main() {
	http.HandleFunc("/motherinfo", func(w http.ResponseWriter, r *http.Request) {
		if err := mother_info_template.Execute(w, nil); err != nil {
			log.Fatal(err)
		}
	})
	http.HandleFunc("/dadinfo", func(w http.ResponseWriter, r *http.Request) {
		if err := dad_info_template.Execute(w, nil); err != nil {
			log.Fatal(err)
		}
	})
	http.HandleFunc("/childinfo", func(w http.ResponseWriter, r *http.Request) {
		if err := child_info_template.Execute(w, nil); err != nil {
			log.Fatal(err)
		}
	})
	http.HandleFunc("/visitinfo", func(w http.ResponseWriter, r *http.Request) {
		if err := visit_info_template.Execute(w, nil); err != nil {
			log.Fatal(err)
		}
	})
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if err := main_template.Execute(w, nil); err != nil {
			log.Fatal(err)
		}
	})
	log.Fatal(http.ListenAndServe(":5173", nil))
}
