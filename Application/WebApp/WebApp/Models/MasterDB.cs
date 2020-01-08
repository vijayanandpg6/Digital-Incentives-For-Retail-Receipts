using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApp.Models
{
    public class MasterDB
    {
        public Retailers[] RetailersList { get; set; }
    }

    public class Retailers
    {
        public string retailerName { get; set; }
        public Dictionary<string, int>[] Products { get; set; }
    }
}