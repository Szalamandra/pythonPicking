using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace fogaszat
{
    class FoglalasokListazasa : Form 
    {
        ListBox lista = new ListBox();
        Button beolvas = new Button();
        Button bezargomb = new Button();

        public FoglalasokListazasa()
        {
            this.Size = new Size(400,400);
            this.Text = "A páciensek által választott kezelések";

            lista.Location = new Point(10,10);
            lista.Size = new Size(350,200);

            beolvas.Text = "Beolvasás";
            beolvas.Location = new Point(30,230);
            beolvas.Click += new EventHandler(Megnyit);

            bezargomb.Text = "Vissza";
            bezargomb.Location = new Point(200, 230);
            bezargomb.Click += new EventHandler(Bezaras);

            lista.Items.Clear();
            string[] fajlbololvas = File.ReadAllLines("foglalasok.txt");

            for (int i = 0; i < fajlbololvas.Length; i++)
            {              
                lista.Items.Add(fajlbololvas[i]);
            }

            Controls.Add(lista);
            Controls.Add(beolvas);
            Controls.Add(bezargomb);
        }

        private void Bezaras(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Megnyit(object sender, EventArgs e)
        {
            lista.Items.Clear();
            OpenFileDialog of = new OpenFileDialog();
            DialogResult dr = of.ShowDialog();
            if (dr == DialogResult.OK)
            {
                if (of.FileName.Contains("foglalasok.txt"))
                {

                    string[] fajlbololvas = File.ReadAllLines("foglalasok.txt");

                    for (int i = 0; i < fajlbololvas.Length; i++)
                    {
                        //string[] seged = fajlbololvas[i].Split(';');

                        lista.Items.Add(fajlbololvas[i]);

                    }
                }
                else MessageBox.Show("Nem a foglalasok.txt-t választottad ki.", "Figyelmeztetés",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
                //string[] fajlbololvas = File.ReadAllLines(of.FileName);

            }
        }
    }

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            adatbetoltes();
        }

        struct paciensadatok
        {
            public string nev;
            public string szigszam;
        }
        paciensadatok[] paciensek = new paciensadatok[50];
        string[] kezelesek = new string[50];
        string[] fogorvosok = new string[10];
        int dbp,dbk,dbo,dbf = 0;

        struct foglalasadatok
        {
            public string nev;
            public string kezeles;
            public string orvos;
        }
        foglalasadatok[] foglalasok = new foglalasadatok[50];

        private void adatbetoltes()
        {
            string[] fajlbol1 = File.ReadAllLines("paciensek.txt");

            for (int i = 0; i < fajlbol1.Length; i++)
            {
                string[] seged = fajlbol1[i].Split('\t');
                paciensek[dbp].nev = seged[0];
                paciensek[dbp].szigszam = seged[1];
                comboBoxpaciensek.Items.Add(paciensek[dbp].nev);
                dbp++;
            }

            string[] fajlbol2 = File.ReadAllLines("kezelesek.txt");

            for (int i = 0; i < fajlbol2.Length; i++)
            {
                kezelesek[dbk] = fajlbol2[i];
                comboBoxkezelesek.Items.Add(kezelesek[dbk]);
                dbk++;
            }

            string[] fajlbol3 = File.ReadAllLines("fogorvosok.txt");
            for (int i = 0; i < fajlbol3.Length; i++)
            {
                fogorvosok[dbo] = fajlbol3[i];
                comboBoxfogorvosok.Items.Add(fajlbol3[i]);
                dbo++;
            }
        }

        private void mentésFájlbaToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            FileStream fajlba = new FileStream("foglalasok.txt",FileMode.Create);
            StreamWriter f_iro = new StreamWriter(fajlba, Encoding.UTF8);
            for (int i = 0; i < dbf; i++)
            {
                f_iro.WriteLine("{0};{1};{2}", foglalasok[i].nev, foglalasok[i].kezeles, foglalasok[i].orvos);
            }
            f_iro.Close();
            fajlba.Close();
            MessageBox.Show("Az aktív foglalásokat kimentettem a foglalasok.txt-be.","Tájékoztatás",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void mentésFájlbaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FileStream fajlba2 = new FileStream("paciensek2.txt", FileMode.Create);
            StreamWriter f_iro2 = new StreamWriter(fajlba2, Encoding.UTF8);
            for (int i = 0; i < dbp; i++)
            {
                f_iro2.WriteLine("{0}\t{1}", paciensek[i].nev,paciensek[i].szigszam);
            }
            f_iro2.Close();
            fajlba2.Close();
            MessageBox.Show("A páciensek adatait kimentettem a paciensek2.txt-be.", "Tájékoztatás",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void buttonfoglalo_Click(object sender, EventArgs e)
        {
            if (comboBoxpaciensek.SelectedItem.ToString() != "" && comboBoxkezelesek.SelectedItem.ToString() != "" && comboBoxfogorvosok.SelectedItem.ToString() != "") 
            { 
            foglalasok[dbf].nev = comboBoxpaciensek.SelectedItem.ToString();
            foglalasok[dbf].kezeles = comboBoxkezelesek.SelectedItem.ToString();
            foglalasok[dbf].orvos = comboBoxfogorvosok.SelectedItem.ToString();

            labelvalasztottpaciens.Text = comboBoxpaciensek.SelectedItem.ToString();
            labelvalasztottkezeles.Text = comboBoxkezelesek.SelectedItem.ToString();
            labelvalasztottorvos.Text = comboBoxfogorvosok.SelectedItem.ToString();

            labelvalasztottpaciens.Visible = true;
            labelvalasztottkezeles.Visible = true;
            labelvalasztottorvos.Visible = true;
            
            dbf++;

            MessageBox.Show("A kiválasztott páciens foglalását rögzítettem.", "Tájékoztatás",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void újPáciensBeviteleToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Formujpaciens ujpaciensfelvitel = new Formujpaciens();
            DialogResult formresult = ujpaciensfelvitel.ShowDialog();

            ujpaciensfelvitel.StartPosition = FormStartPosition.CenterScreen;
            string nev, szigszam = "";
            ujpaciensfelvitel.Beolvas(out nev,out szigszam);
            if (formresult == DialogResult.OK && nev != "" && szigszam != "")
            {
                paciensek[dbp].nev = nev;
                paciensek[dbp].szigszam = szigszam;

                comboBoxpaciensek.Items.Add(paciensek[dbp].nev);
                comboBoxpaciensek.Sorted = comboBoxpaciensek.Sorted = true;

                dbp++;
            }
            else MessageBox.Show("Minden mezőt ki kell tölteni!", "Figyelmeztetés",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        private void foglalásokListázásaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FoglalasokListazasa ujform = new FoglalasokListazasa();
            ujform.ShowDialog();
        }

        private void újFoglalásToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                if (comboBoxpaciensek.SelectedItem.ToString() != "" && comboBoxkezelesek.SelectedItem.ToString() != "" && comboBoxfogorvosok.SelectedItem.ToString() != "")
                {
                    foglalasok[dbf].nev = comboBoxpaciensek.SelectedItem.ToString();
                    foglalasok[dbf].kezeles = comboBoxkezelesek.SelectedItem.ToString();
                    foglalasok[dbf].orvos = comboBoxfogorvosok.SelectedItem.ToString();

                    labelvalasztottpaciens.Text = comboBoxpaciensek.SelectedItem.ToString();
                    labelvalasztottkezeles.Text = comboBoxkezelesek.SelectedItem.ToString();
                    labelvalasztottorvos.Text = comboBoxfogorvosok.SelectedItem.ToString();

                    labelvalasztottpaciens.Visible = true;
                    labelvalasztottkezeles.Visible = true;
                    labelvalasztottorvos.Visible = true;
                    dbf++;

                    MessageBox.Show("A kiválasztott páciens foglalását rögzítettem.", "Tájékoztatás",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
            catch
            {
                MessageBox.Show("Mindenhol válassz ki egy lehetőséget.", "Figyelmeztetés",MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }


        private void kilépésToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            Close();
        }
    }

}
