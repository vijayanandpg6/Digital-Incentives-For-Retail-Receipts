using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Web;
using WebApp.Models;

namespace WebApp.Client
{
    public static class HttpClientHelper
    {
        public static string BaseURL = "http://localhost:5000/";
        public static void SegmentImages()
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(BaseURL + "segmentObject/");
            request.Method = "GET";
            request.ContentType = "application/json";
            //request.ContentLength = DATA.Length;
            //using (Stream webStream = request.GetRequestStream())

            try
            {
                WebResponse webResponse = request.GetResponse();
                using (Stream webStream = webResponse.GetResponseStream() ?? Stream.Null)
                using (StreamReader responseReader = new StreamReader(webStream))
                {
                    string response = responseReader.ReadToEnd();
                }
            }
            catch (Exception e)
            {

            }

        }

        public static MatchedProduct ProductMatcher(string product)
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(BaseURL + "productMatch/" + Uri.EscapeDataString(product));
            request.Method = "GET";
            request.ContentType = "application/json";
            //request.ContentLength = DATA.Length;
            //using (Stream webStream = request.GetRequestStream())

            try
            {
                WebResponse webResponse = request.GetResponse();
                using (Stream webStream = webResponse.GetResponseStream() ?? Stream.Null)
                using (StreamReader responseReader = new StreamReader(webStream))
                {
                    string response = responseReader.ReadToEnd();
                    JObject json = JObject.Parse(response);
                    var productObj = JsonConvert.DeserializeObject<MatchedProduct>(json["data"].ToString());
                    if (productObj.ProductID == 0)
                        return null;
                    else
                        return productObj;
                }
            }
            catch (Exception e)
            {
                return null;
            }

        }

        public static string CompanyMatcher(string company)
        {
            string companyName = company;
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(BaseURL + "companyMatch/" + Uri.EscapeDataString(company));
            request.Method = "GET";
            request.ContentType = "application/json";
            //request.ContentLength = DATA.Length;
            //using (Stream webStream = request.GetRequestStream())

            try
            {
                WebResponse webResponse = request.GetResponse();
                using (Stream webStream = webResponse.GetResponseStream() ?? Stream.Null)
                using (StreamReader responseReader = new StreamReader(webStream))
                {
                    string response = responseReader.ReadToEnd();
                    JObject json = JObject.Parse(response);
                    companyName = json["data"].ToString();
                    return companyName;
                }
            }
            catch (Exception e)
            {
                return companyName;
            }

        }

    }
}