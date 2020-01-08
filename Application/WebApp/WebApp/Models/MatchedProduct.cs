using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApp.Models
{
    public class MatchedProduct
    {
        public int? ProductID { get; set; }
        public string ProductMasterName { get; set; }
        public string ProductName { get; set; }
        public string ProductTerm { get; set; }
        public int ProductAccuracy { get; set; }
    }
}