
%%
% 
%  This is the matlab file to compute tilt angles from raw accelerometer
%  data. During the genration of this code, we computed the tilt angles
%  for rw acceleromter data captured by AIM-v2 device. Here the data was
%  saved as a bin file. one may recode the bin file input to csv or any
%  data file type inteded. Also, pay attention to the axis of the
%  acceleromter. The axis may be prelablled by manifacture. if not, do a
%  calibration test determine xyz.


clear all

Roll = [];
Pitch = [];
x1 = [];
y1 = [];
z1 = [];
dinfo = dir('*.JPG');

Folder = cd;




[file,path] = uigetfile('*.bin');

filename=fullfile(path,file);

[acc_data_x_128Hz, acc_data_y_128Hz, acc_data_z_128Hz, bend_data_128Hz, AIM_Date,AIM_Time,AIM_Data ] = extract_AIM_data(filename);
 
temp = erase( char(file),".BIN");

dinfo = dir('*.JPG');
Name = {dinfo.name};

for i = 1 : numel(Name)
T1 = (hex2dec(temp));
T2 = str2num((erase(char(Name{i}),".JPG")));

TD = T2-T1;
TDn = TD - 0.5;
idx1 = TDn * 128;
idx2 = idx1 + 127;

x = acc_data_x_128Hz(idx1:idx2);
z = acc_data_y_128Hz(idx1:idx2);
y = acc_data_z_128Hz(idx1:idx2);

    for j = 1:numel(x)

        Gpx = x(j);
        Gpy = y(j);
        Gpz = z(j);

       Pitch1(j,:)= atand(-Gpx/(sqrt(Gpy^2+Gpz^2)));

       mu = 0.01;
       Roll1(j,:)= atand(Gpy/ (abs(Gpz)*(sqrt(Gpz^2+mu*(Gpx^2)))));
       
    end

R =  mean(Roll1);
P =  mean(Pitch1);


    
Roll = [Roll R];
Pitch = [Pitch P];
x1 = [x1 mean(x)];
y1 = [y1 mean(y)];
z1 = [z1 mean(z)];


end



