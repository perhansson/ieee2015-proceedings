from ROOT import TFile, TH1F, TCanvas, TLatex

def myText(x,y,text, tsize,color):
    l = TLatex()
    l.SetTextSize(tsize); 
    l.SetNDC();
    l.SetTextColor(color);
    l.DrawLatex(x,y,text);

tfile_mc = TFile('tritrig-norm-plots.root')
tfile_data = TFile('golden-norm-plots.root')

h_mc = tfile_mc.Get('slice_36')
h_data = tfile_data.Get('slice_36')

print h_mc.GetXaxis().GetBinWidth(1)
print h_data.GetXaxis().GetBinWidth(1)

n_data = h_data.Integral()
n_mc = h_mc.Integral()
print n_data, ' , ', n_mc
h_mc.Scale(n_data/n_mc)

c = TCanvas('c','c',10,10,700,500)
h_mc.SetTitle(";Radiative vertex z (mm);Arbitrary units")
h_mc.GetXaxis().SetTitleSize(0.05)
h_mc.GetYaxis().SetTitleSize(0.05)
h_mc.GetYaxis().SetTitleOffset(0.8)
h_mc.SetStats(False)
h_mc.SetFillColor(17)
h_mc.Draw("hist")
h_data.SetMarkerStyle(20)
h_data.SetMarkerSize(1.0)
h_data.Draw("same")
myText(0.58,0.84,'m_{e^{+}e^{-}} = 38.5-42.9 MeV',0.05,1)
myText(0.15,0.8,'Preliminary',0.08,2)
c.SetLogy(True)
c.SaveAs('overlay-slice-36-pelle.png')
ans = raw_input('cont')

