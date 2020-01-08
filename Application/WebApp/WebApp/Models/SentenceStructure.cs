using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApp.Models
{
    public class SentenceStructure
    {
        public string Sentence { get; set; }
        public List<TextStructure> TextStructureParis { get; set; }
    }
}