from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    """
    Currency conversion tool (NZD to AUD or AUD to NZD)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.to_history_button = Button(self.currency_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialogue box and disables history button (so that users can't create multiple history boxes)
        """
        ExportHistory(self)


class ExportHistory:

    def __init__(self, partner):
        # setup dialogue box and background colour

        green_back = "#D5E8D4"
        peach_back = "#ffe6cc"

        self.history_box = Toplevel()

        # disable help button
        partner.to_history_button.config(state=DISABLED)

        # IF users press the cross at the top, closes help and 'releases' help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # strings for 'long' tables...
        recent_intro_txt = ("blah blah information stuff")

        export_instruction_txt = ("export this")

        calculations = ""

        # LAbel list text, format, bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            ["calculations list", ("Arial", "14"), green_back],
            [export_instruction_txt, ("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # retrieve export instruction label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame to hold buttons (two columns)
        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        button_ref_list = []

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#004C99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.history_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def close_history(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()
