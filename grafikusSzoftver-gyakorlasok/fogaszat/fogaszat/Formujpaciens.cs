using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace fogaszat
{
    public partial class Formujpaciens : Form
    {
        public Formujpaciens()
        {
            InitializeComponent();
        }

        private void Formujpaciens_Load(object sender, EventArgs e)
        {
            buttonOK.DialogResult = DialogResult.OK;
            buttonmegse.DialogResult = DialogResult.Cancel;
            this.AcceptButton = buttonOK;
            this.CancelButton = buttonmegse;
        }

        public void Beolvas(out string paciensneve, out string szszam)
        {
            paciensneve = textBox1.Text;
            szszam = textBox2.Text;
        }
    }
}
