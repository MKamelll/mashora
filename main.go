package main

import (
	"html/template"
	"log"
	"net/http"
)

func parseTemplate(name string) *template.Template {
	tmpl, err := template.ParseFiles(
		"templates/base.tmpl",
		"templates/"+name+".tmpl",
	)

	if err != nil {
		log.Fatal("template parsing error " + err.Error())
	}

	return tmpl
}

var (
	mother_info_template   = parseTemplate("motherinfo")
	dad_info_template      = parseTemplate("dadinfo")
	child_info_template    = parseTemplate("childinfo")
	visit_info_template    = parseTemplate("visitinfo")
	visit_topics_template  = parseTemplate("visittopics")
	index_template         = parseTemplate("index")
	general_template       = parseTemplate("general")
	child_mashora_template = parseTemplate("childmashora")
)

type IndexData struct {
	Name string
}

type MotherInfo struct {
	Name        string
	NationalId  string
	PhoneNumber string
}

func is_htmx(r *http.Request) bool {
	return r.Header.Get("HX-Request") == "true"
}

func redirect_to_root(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "/", http.StatusSeeOther)
}

func handleMotherInfo(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}
	if err := mother_info_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func handleDadInfo(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}
	if err := dad_info_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func handleChildInfo(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}
	if err := child_info_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func handleVisitInfo(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}
	if err := visit_info_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func handleVisitTopics(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}
	if err := visit_topics_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func handleGeneral(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}
	if err := general_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func handleChildMashora(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}
	if err := child_mashora_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func handleSubmitGeneral(w http.ResponseWriter, r *http.Request) {
	if !is_htmx(r) {
		redirect_to_root(w, r)
	}

	if r.Method != http.MethodPost {
		redirect_to_root(w, r)
	}

	if err := r.ParseForm(); err != nil {
		http.Error(w, "Error parsing the form", http.StatusBadRequest)
		return
	}

	mashora_kind := r.FormValue("mashora_kind")

	switch mashora_kind {
	case "for-child":
		handleChildMashora(w, r)
	default:
		handleIndex(w, r)
	}
}

func handleIndex(w http.ResponseWriter, r *http.Request) {
	if err := index_template.ExecuteTemplate(w, "base.tmpl", nil); err != nil {
		log.Fatal(err)
	}
}

func main() {
	http.HandleFunc("/motherinfo", handleMotherInfo)
	http.HandleFunc("/dadinfo", handleDadInfo)
	http.HandleFunc("/childinfo", handleChildInfo)
	http.HandleFunc("/visitinfo", handleVisitInfo)
	http.HandleFunc("/visittopics", handleVisitTopics)
	http.HandleFunc("/general", handleGeneral)
	http.HandleFunc("/childmashora", handleChildMashora)
	http.HandleFunc("/submitgeneral", handleSubmitGeneral)
	http.HandleFunc("/", handleIndex)

	log.Fatal(http.ListenAndServe(":5173", nil))
}
