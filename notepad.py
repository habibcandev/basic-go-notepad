package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
)

type Note struct {
	ID    int    `json:"id"`
	Title string `json:"title"`
	Body  string `json:"body"`
}

var notes []Note
var lastID = 0

func main() {
	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/notes", notesHandler)
	http.HandleFunc("/add", addHandler)
	http.HandleFunc("/edit/", editHandler)
	http.HandleFunc("/delete/", deleteHandler)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	fmt.Printf("Server running on port %s...\n", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to Simple Notes App!")
}

func notesHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(notes)
}

func addHandler(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "Error reading request body", http.StatusBadRequest)
		return
	}

	var note Note
	err = json.Unmarshal(body, &note)
	if err != nil {
		http.Error(w, "Invalid JSON format", http.StatusBadRequest)
		return
	}

	lastID++
	note.ID = lastID
	notes = append(notes, note)

	w.WriteHeader(http.StatusCreated)
}

func editHandler(w http.ResponseWriter, r *http.Request) {
	parts := strings.Split(r.URL.Path, "/")
	idStr := parts[len(parts)-1]
	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Redirect(w, r, "/", http.StatusSeeOther)
		return
	}

	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "Error reading request body", http.StatusBadRequest)
		return
	}

	var updateNote Note
	err = json.Unmarshal(body, &updateNote)
	if err != nil {
		http.Error(w, "Invalid JSON format", http.StatusBadRequest)
		return
	}

	for i, note := range notes {
		if note.ID == id {
			notes[i].Title = updateNote.Title
			notes[i].Body = updateNote.Body
			return
		}
	}

	http.Redirect(w, r, "/", http.StatusSeeOther)
}

func deleteHandler(w http.ResponseWriter, r *http.Request) {
	parts := strings.Split(r.URL.Path, "/")
	idStr := parts[len(parts)-1]
	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Redirect(w, r, "/", http.StatusSeeOther)
		return
	}

	for i, note := range notes {
		if note.ID == id {
			notes = append(notes[:i], notes[i+1:]...)
			return
		}
	}

	http.Redirect(w, r, "/", http.StatusSeeOther)
}

