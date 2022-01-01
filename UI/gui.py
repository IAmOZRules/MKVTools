import Neutron

win = Neutron.Window("MKVTools", size=(800, 800), css="styles.css")
win.display(file="index.html")


def onClick():
    win.preventDefault()
    imdbCode = win.getElementsByName("imdbCode").value
    seasonRange = win.getElementById("seasonRange").value
    episodeDirectory = win.getElementById("episodeDirectory").value
    subtitleDirectory = win.getElementById("subtitleDirectory").value
    print(imdbCode, seasonRange, episodeDirectory, subtitleDirectory)

win.getElementById("submit").addEventListener("click", Neutron.event(onClick))

win.show()