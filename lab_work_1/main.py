from ui import UI
from pdoc import html

if __name__ == "__main__":
    html1 = html("directed_graph")
    f1 = open("directed_graph.html", "wt")
    f1.write(html1)

    html2 = html("operations")
    f2 = open("operations.html", "wt")
    f2.write(html2)

    html3 = html("utilities")
    f3 = open("utilities.html", "wt")
    f3.write(html3)

    app = UI()
    app.run()