from PyQt5.QtWidgets import QApplication
import sys

from RKIAnalyzer import RKIAnalyzer
from gui import App


def plotFunction(ax, choice):
    """
    Diese Funktion wird aufgerufen, wenn der Benutzer ein anderes Bundesland wählt oder direkt nach dem Start.
    :param ax: Matplotlib Ax-Objekt. Mit z. b. ax.plot kann gezeichnet werden.
    :param bundesland: Name des ausgewählten Bundeslands
    :return: None
    """

    if (choice == 'AnzahlFall'):
        dataIll = analyzer.getWeeklySumOfAllData(columnName='AnzahlFall')  # maghadire nemudar migire az getWeek... az RKI Analiz
        ax.plot(dataIll.index, dataIll, label=choice)  # plot misaze azash
        dataDead = analyzer.getWeeklySumOfAllData(columnName='AnzahlTodesfall')
        ax.plot(dataDead.index, dataDead, label='AnzahlTodesfall')

        # sharedDataBundesland=analyzer.getWeeklyCumulatedDataForAnzahfall(columnName='Bundesland')
        # sharedDataDatum=analyzer.getWeeklyCumulatedDataForAnzahfall(columnName='Bundesland')

        ax.set_title('Tod- und Anzahlfälle')
        ax.legend()
        ax.grid()
    else:
        dataIll = analyzer.getWeeklySumOfEachSexuality(columnName='AnzahlFall', sexualityTarget=choice)
        ax.plot(dataIll.index, dataIll, label=choice)

        # sharedDataBundesland = analyzer.getWeeklyCumulatedDataForAnzahfall(columnName='Bundesland')
        # sharedDataDatum = analyzer.getWeeklyCumulatedDataForAnzahfall(columnName='Bundesland')

        ax.set_title('Männer/Frauen/Unbekannt')
        ax.legend()
        ax.grid()

def guiReadyFunction(window):
    """
    Wird aufgerufen, wenn alle Elemente der GUI aufgebaut sind.
    :param window: Verweis auf das GUI-Fenster. Hiermit kann z. B. die Statuszeile verändert werden.
    :return: None
    """
    window.showStatusText("Lese Daten. Bitte warten....", executeEventLoop=True)

    fn = '../daten/RKI_COVID19_short.csv'  # import etelaat az file
    analyzer.loadDataFromFile(fn, filetype='csv')

    window.setter(analyzer.getBundesland(), analyzer.getDate())
    window.showStatusText("Bereit")

if __name__ == '__main__':
    analyzer = RKIAnalyzer()  # todo , IN NEMIDOONAM CHIKAR MIKONE

    app = QApplication(sys.argv)
    w = App(plotFunction=plotFunction, guiReadyFunction=guiReadyFunction)

    # App(plotFunction=plotFunctionAnzahl,guiReadyFunction=guiReadyFunction)  # Starte Mane injas, ke ettelaat mire be Classe App az GUI # todo inja oomadim bokonimesh dota plotfunction
    # App(plotFunction=plotFunctionTodes, guiReadyFunction=guiReadyFunction)
    sys.exit(app.exec_())
