
namespace fogaszat
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.foglalásToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.újFoglalásToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.foglalásokListázásaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mentésFájlbaToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.páciensekToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.újPáciensBeviteleToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mentésFájlbaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.kilépésToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.comboBoxpaciensek = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.labelvalasztottpaciens = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.comboBoxkezelesek = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.comboBoxfogorvosok = new System.Windows.Forms.ComboBox();
            this.labelvalasztottkezeles = new System.Windows.Forms.Label();
            this.labelvalasztottorvos = new System.Windows.Forms.Label();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.buttonfoglalo = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.foglalásToolStripMenuItem,
            this.páciensekToolStripMenuItem,
            this.kilépésToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(519, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // foglalásToolStripMenuItem
            // 
            this.foglalásToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.újFoglalásToolStripMenuItem,
            this.foglalásokListázásaToolStripMenuItem,
            this.mentésFájlbaToolStripMenuItem1});
            this.foglalásToolStripMenuItem.Name = "foglalásToolStripMenuItem";
            this.foglalásToolStripMenuItem.Size = new System.Drawing.Size(75, 20);
            this.foglalásToolStripMenuItem.Text = "Foglalások";
            // 
            // újFoglalásToolStripMenuItem
            // 
            this.újFoglalásToolStripMenuItem.Name = "újFoglalásToolStripMenuItem";
            this.újFoglalásToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.újFoglalásToolStripMenuItem.Text = "Új foglalás";
            this.újFoglalásToolStripMenuItem.Click += new System.EventHandler(this.újFoglalásToolStripMenuItem_Click);
            // 
            // foglalásokListázásaToolStripMenuItem
            // 
            this.foglalásokListázásaToolStripMenuItem.Name = "foglalásokListázásaToolStripMenuItem";
            this.foglalásokListázásaToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.foglalásokListázásaToolStripMenuItem.Text = "Foglalások listázása";
            this.foglalásokListázásaToolStripMenuItem.Click += new System.EventHandler(this.foglalásokListázásaToolStripMenuItem_Click);
            // 
            // mentésFájlbaToolStripMenuItem1
            // 
            this.mentésFájlbaToolStripMenuItem1.Name = "mentésFájlbaToolStripMenuItem1";
            this.mentésFájlbaToolStripMenuItem1.Size = new System.Drawing.Size(180, 22);
            this.mentésFájlbaToolStripMenuItem1.Text = "Mentés fájlba";
            this.mentésFájlbaToolStripMenuItem1.Click += new System.EventHandler(this.mentésFájlbaToolStripMenuItem1_Click);
            // 
            // páciensekToolStripMenuItem
            // 
            this.páciensekToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.újPáciensBeviteleToolStripMenuItem,
            this.mentésFájlbaToolStripMenuItem});
            this.páciensekToolStripMenuItem.Name = "páciensekToolStripMenuItem";
            this.páciensekToolStripMenuItem.Size = new System.Drawing.Size(71, 20);
            this.páciensekToolStripMenuItem.Text = "Páciensek";
            // 
            // újPáciensBeviteleToolStripMenuItem
            // 
            this.újPáciensBeviteleToolStripMenuItem.Name = "újPáciensBeviteleToolStripMenuItem";
            this.újPáciensBeviteleToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.újPáciensBeviteleToolStripMenuItem.Text = "Új páciens felvitele";
            this.újPáciensBeviteleToolStripMenuItem.Click += new System.EventHandler(this.újPáciensBeviteleToolStripMenuItem_Click);
            // 
            // mentésFájlbaToolStripMenuItem
            // 
            this.mentésFájlbaToolStripMenuItem.Name = "mentésFájlbaToolStripMenuItem";
            this.mentésFájlbaToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.mentésFájlbaToolStripMenuItem.Text = "Mentés fájlba";
            this.mentésFájlbaToolStripMenuItem.Click += new System.EventHandler(this.mentésFájlbaToolStripMenuItem_Click);
            // 
            // kilépésToolStripMenuItem
            // 
            this.kilépésToolStripMenuItem.Name = "kilépésToolStripMenuItem";
            this.kilépésToolStripMenuItem.Size = new System.Drawing.Size(56, 20);
            this.kilépésToolStripMenuItem.Text = "Kilépés";
            this.kilépésToolStripMenuItem.Click += new System.EventHandler(this.kilépésToolStripMenuItem_Click);
            // 
            // comboBoxpaciensek
            // 
            this.comboBoxpaciensek.FormattingEnabled = true;
            this.comboBoxpaciensek.Location = new System.Drawing.Point(28, 67);
            this.comboBoxpaciensek.Name = "comboBoxpaciensek";
            this.comboBoxpaciensek.Size = new System.Drawing.Size(218, 21);
            this.comboBoxpaciensek.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.label1.Location = new System.Drawing.Point(31, 43);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(70, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Páciensek:";
            // 
            // labelvalasztottpaciens
            // 
            this.labelvalasztottpaciens.AutoSize = true;
            this.labelvalasztottpaciens.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.labelvalasztottpaciens.Location = new System.Drawing.Point(316, 53);
            this.labelvalasztottpaciens.Name = "labelvalasztottpaciens";
            this.labelvalasztottpaciens.Size = new System.Drawing.Size(41, 13);
            this.labelvalasztottpaciens.TabIndex = 3;
            this.labelvalasztottpaciens.Text = "label2";
            this.labelvalasztottpaciens.Visible = false;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.label3.Location = new System.Drawing.Point(31, 121);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(69, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Kezelések:";
            // 
            // comboBoxkezelesek
            // 
            this.comboBoxkezelesek.FormattingEnabled = true;
            this.comboBoxkezelesek.Location = new System.Drawing.Point(28, 145);
            this.comboBoxkezelesek.Name = "comboBoxkezelesek";
            this.comboBoxkezelesek.Size = new System.Drawing.Size(218, 21);
            this.comboBoxkezelesek.TabIndex = 4;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.label4.Location = new System.Drawing.Point(31, 201);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(63, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "Fogorvos:";
            // 
            // comboBoxfogorvosok
            // 
            this.comboBoxfogorvosok.FormattingEnabled = true;
            this.comboBoxfogorvosok.Location = new System.Drawing.Point(28, 225);
            this.comboBoxfogorvosok.Name = "comboBoxfogorvosok";
            this.comboBoxfogorvosok.Size = new System.Drawing.Size(218, 21);
            this.comboBoxfogorvosok.TabIndex = 6;
            // 
            // labelvalasztottkezeles
            // 
            this.labelvalasztottkezeles.AutoSize = true;
            this.labelvalasztottkezeles.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.labelvalasztottkezeles.Location = new System.Drawing.Point(316, 104);
            this.labelvalasztottkezeles.Name = "labelvalasztottkezeles";
            this.labelvalasztottkezeles.Size = new System.Drawing.Size(41, 13);
            this.labelvalasztottkezeles.TabIndex = 9;
            this.labelvalasztottkezeles.Text = "label5";
            this.labelvalasztottkezeles.Visible = false;
            // 
            // labelvalasztottorvos
            // 
            this.labelvalasztottorvos.AutoSize = true;
            this.labelvalasztottorvos.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.labelvalasztottorvos.Location = new System.Drawing.Point(316, 153);
            this.labelvalasztottorvos.Name = "labelvalasztottorvos";
            this.labelvalasztottorvos.Size = new System.Drawing.Size(41, 13);
            this.labelvalasztottorvos.TabIndex = 10;
            this.labelvalasztottorvos.Text = "label6";
            this.labelvalasztottorvos.Visible = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Image = global::fogaszat.Properties.Resources.fog;
            this.pictureBox2.Location = new System.Drawing.Point(319, 201);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(167, 167);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox2.TabIndex = 11;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::fogaszat.Properties.Resources.exit_picture;
            this.pictureBox1.Location = new System.Drawing.Point(197, 320);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(69, 62);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Click += new System.EventHandler(this.pictureBox1_Click);
            // 
            // buttonfoglalo
            // 
            this.buttonfoglalo.Location = new System.Drawing.Point(34, 279);
            this.buttonfoglalo.Name = "buttonfoglalo";
            this.buttonfoglalo.Size = new System.Drawing.Size(110, 38);
            this.buttonfoglalo.TabIndex = 12;
            this.buttonfoglalo.Text = "Foglalj orvost!";
            this.buttonfoglalo.UseVisualStyleBackColor = true;
            this.buttonfoglalo.Click += new System.EventHandler(this.buttonfoglalo_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.label2.Location = new System.Drawing.Point(31, 369);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 13);
            this.label2.TabIndex = 13;
            this.label2.Text = "label2";
            this.label2.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(519, 409);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.buttonfoglalo);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.labelvalasztottorvos);
            this.Controls.Add(this.labelvalasztottkezeles);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.comboBoxfogorvosok);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.comboBoxkezelesek);
            this.Controls.Add(this.labelvalasztottpaciens);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.comboBoxpaciensek);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.MaximumSize = new System.Drawing.Size(535, 448);
            this.MinimumSize = new System.Drawing.Size(535, 448);
            this.Name = "Form1";
            this.Text = "Fogászati kezelések";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem kilépésToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem foglalásToolStripMenuItem;
        private System.Windows.Forms.ComboBox comboBoxpaciensek;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label labelvalasztottpaciens;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox comboBoxkezelesek;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ComboBox comboBoxfogorvosok;
        private System.Windows.Forms.ToolStripMenuItem újFoglalásToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem foglalásokListázásaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mentésFájlbaToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem páciensekToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem újPáciensBeviteleToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mentésFájlbaToolStripMenuItem;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label labelvalasztottkezeles;
        private System.Windows.Forms.Label labelvalasztottorvos;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Button buttonfoglalo;
        private System.Windows.Forms.Label label2;
    }
}

