def add_movie():
    print("Enter the details")
    details = input("Title\tDirector\tRelease Year")
    title, director, release = details.split();
    movies.append(
        {'Title': title.upper(), 'Director': director.upper(), 'Release Year': release}
    )
    print(f"{title} is added to the list\n")


def list_all():
    for movie in movies:
        print(f"Title of the movie:- {movie['Title']}\nName of the Director:- {movie['Director']}\nRelease Year:- {movie['Release Year']}\n")


def check_movie():
    title = input('Enter the title of the movie')
    Title = title.upper();
    for movie in movies:
        if movie['title'] == Title:
            print(f"Title of the movie:- {movie['Title']}\nName of the Director:- {movie['Director']}\nRelease Year:- {movie['Release Year']}\n")
            return
    print(f'{title} is not found in the list of movies\n')
    check = input("Do you want to check the movie list ?").lower()
    if check == 'yes':
        list_all()


def delete_movie():
    title = input("Enter the title of the movie to be deleted").upper()
    for movie in movies:
        if movie['title'] == title:
            movies.remove(movie)
            print(f"Deleted {title} from the list\n")
            return
    print(f"{title} not found in the movie list\n")


movies = []
choice = 'y'
while choice != 'q':
    print("Select the required operation")
    print("1.Added a Movie\n2.List all the movies\n3.Check for a Movie\n4.Delete a Movie\nq.Exit the app\n")
    option = (input())
    match option:
        case "1":
            add_movie()
        case "2":
            list_all()
        case "3":
            check_movie()
        case "4":
            delete_movie()
        case "q":
            print("Thank you for using the app")
            choice = 'q'
