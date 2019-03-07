// -*- C++ -*-
//
// generated by wxGlade
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

#ifndef BUG183_H
#define BUG183_H

#include <wx/wx.h>
#include <wx/image.h>
#include <wx/intl.h>

#ifndef APP_CATALOG
#define APP_CATALOG "app"  // replace with the appropriate catalog name
#endif


// begin wxGlade: ::dependencies
// end wxGlade

// begin wxGlade: ::extracode
// end wxGlade


class Bug183_UI_Frame: public wxFrame {
public:
    // begin wxGlade: Bug183_UI_Frame::ids
    // end wxGlade

    Bug183_UI_Frame(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos=wxDefaultPosition, const wxSize& size=wxDefaultSize, long style=wxDEFAULT_FRAME_STYLE);

private:
    // begin wxGlade: Bug183_UI_Frame::methods
    void set_properties();
    void do_layout();
    // end wxGlade

protected:
    // begin wxGlade: Bug183_UI_Frame::attributes
    wxStaticText* label_1;
    // end wxGlade
}; // wxGlade: end class


class Bug173_UI_SomeDialog: public wxDialog {
public:
    // begin wxGlade: Bug173_UI_SomeDialog::ids
    // end wxGlade

    Bug173_UI_SomeDialog(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos=wxDefaultPosition, const wxSize& size=wxDefaultSize, long style=wxDEFAULT_DIALOG_STYLE);

private:
    // begin wxGlade: Bug173_UI_SomeDialog::methods
    void set_properties();
    void do_layout();
    // end wxGlade

protected:
    // begin wxGlade: Bug173_UI_SomeDialog::attributes
    wxStaticText* label_2;
    // end wxGlade
}; // wxGlade: end class


#endif // BUG183_H