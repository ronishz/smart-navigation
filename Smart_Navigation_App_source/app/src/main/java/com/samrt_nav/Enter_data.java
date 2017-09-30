package com.samrt_nav;

import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Color;
import android.os.AsyncTask;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.ads.identifier.AdvertisingIdClient;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.maps.model.PolylineOptions;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import com.google.android.gms.maps.model.Polyline;

public class Enter_data extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;

    ArrayList<String> nms = new ArrayList<String>();
    ArrayList<String> lts = new ArrayList<String>();
    ArrayList<String> las = new ArrayList<String>();
    ArrayList<String> smode = new ArrayList<String>();
    ArrayList<LatLng> points = new ArrayList<LatLng>();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enter_data);
        Intent intent = getIntent();
        Bundle extras = intent.getExtras();
        nms = extras.getStringArrayList(Info.EXTRA_MESSAGEm2);
        lts = extras.getStringArrayList(Info.EXTRA_MESSAGEm3);
        las = extras.getStringArrayList(Info.EXTRA_MESSAGEm4);
        smode = extras.getStringArrayList(Info.EXTRA_MESSAGEm5);


        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }



    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        // Add a marker in Sydney and move the camera
        for(Integer i=0;i<nms.size();i++) {
            Double tlat= Double.parseDouble(lts.get(i));
            Double tlang=Double.parseDouble(las.get(i));
            LatLng syd = new LatLng(tlat,tlang);
            points.add(syd);

            mMap.addMarker(new MarkerOptions().position(syd).title(nms.get(i)+","+smode.get(i)));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(syd));
        }
        LatLng syd1=new LatLng(18.531206,73.855278);
        points.add(syd1);

    }


}
