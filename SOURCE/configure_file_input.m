function parameters = configure_file_input( )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    fileID = fopen('config.txt', 'r');
    tline = fgetl(fileID);
    while ischar(tline)
        tokens = strsplit(tline, '-:::-')
        paraKey = tokens(1,1)
        paraValue = tokens(1,2)
        switch paraKey{1}
            case 'data_dir'
                parameters.data_dir = paraValue{1};
            case 'com_dir'
                parameters.com_dir = paraValue{1};
            case 'tao_dir'
                parameters.tao_dir = paraValue{1};
            case 'fd'
                parameters.fd = str2num(paraValue{1});
            case 'fb'
                parameters.fb = str2num(paraValue{1});
        end
        tline = fgetl(fileID);
    end
    fclose(fileID);
end

