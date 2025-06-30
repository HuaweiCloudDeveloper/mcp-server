# OCR MCP Server 


## Version
v0.1.0

## Overview

OCR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service OCR. Full-chain management of OCR resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="1">Accepted Bill Identification</td>
                    <td>RecognizeAcceptanceBill</td>
                    <td>Identifies key information in the acceptance bill and returns structured results in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Airplane itinerary identification</td>
                    <td>RecognizeFlightItinerary</td>
                    <td>Identifies text information in the aircraft itinerary and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Bank Card OCR</td>
                    <td>RecognizeBankcard</td>
                    <td>Identifies key text information on bank cards and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Bank Receipt Identification</td>
                    <td>RecognizeBankReceipt</td>
                    <td>Supports text recognition and key-value pair extraction for bank receipts, implementing efficient automatic and structured return.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Business Card Recognition</td>
                    <td>RecognizeBusinessCard</td>
                    <td>Identifies the text information on the business card image and returns the structured recognition result. Extracts structured information from business cards in different formats.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Business License Identification</td>
                    <td>RecognizeBusinessLicense</td>
                    <td>Identifies text information in the image on the business license home page and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Colombian Identity Card Identification</td>
                    <td>RecognizeColombiaIdCard</td>
                    <td>Identifies the text information in the Colombian ID card and returns the recognition result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Customized template OCR</td>
                    <td>RecognizeCustomTemplate</td>
                    <td>Customized template OCR: Users can customize templates. For various bills and cards with fixed formats, users can specify key fields to be identified on the GUI to automatically identify and extract images in specific formats.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Document Book Identification</td>
                    <td>RecognizeHouseholdRegister</td>
                    <td>Identifies text information in the household register and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Driver's license recognition</td>
                    <td>RecognizeDriverLicense</td>
                    <td>Identifies the driver's license image uploaded by the user. (or the URL of the driver's license image file on OBS on HUAWEI CLOUD provided by the user) The text content of the homepage and secondary page in the, and the recognition result is returned to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Electronic Sheet Identification</td>
                    <td>RecognizeWaybillElectronic</td>
                    <td>Identifies the text content in the electronic sheet image uploaded by the user and returns the recognition result in JSON format to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Financial Statement Identification</td>
                    <td>RecognizeFinancialStatement</td>
                    <td>Identifies the text in the table image uploaded by the user and returns the recognition result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">General OCR</td>
                    <td>RecognizeGeneralText</td>
                    <td>Recognizes the text information on the image and returns the recognized text and coordinates. Supports text recognition in multiple scenarios, such as scanning files, electronic documents, books, bills, and forms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">General Table Identifier</td>
                    <td>RecognizeGeneralTable</td>
                    <td>Identifies a common table image uploaded by a user. (or URL of the general table image file on OBS on HUAWEI CLOUD provided by the user) Text content in and return the recognition result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Handwritten Character Recognition</td>
                    <td>RecognizeHandwriting</td>
                    <td>Identifies handwritten text information in a document and returns the recognition result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Identity Card Recognition</td>
                    <td>RecognizeIdCard</td>
                    <td>Identifies the text in the ID card image and returns the recognition result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Insurance policy identification</td>
                    <td>RecognizeInsurancePolicy</td>
                    <td>Identifies the text information on the insurance policy image and returns the recognition result to the user. Structured information can be extracted from scanned images and mobile phone photos of insurance policies in multiple formats.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Intelligent classification recognition</td>
                    <td>RecognizeAutoClassification</td>
                    <td>Detects the ticket (ticket, certificate, or other text carrier) specified on the location image to be recognized and performs structured recognition on the ticket. The interface returns the location coordinates of the ticket to be recognized on the image, the content to be recognized in a structured manner, and the corresponding category in a list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Invoice verity</td>
                    <td>RecognizeInvoiceVerification</td>
                    <td>The invoice verification service supports the information verification of 10 types of VAT invoices, including VAT special invoices, VAT ordinary invoices, VAT ordinary invoices (roll-type), VAT electronic special invoices, VAT electronic ordinary invoices, and VAT electronic ordinary invoices (toll)), unified invoice for used car sales, unified invoice for motor vehicle sales, electronic invoice for blockchain, and all-electric invoice. All information about the ticket face can be returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">License plate recognition</td>
                    <td>RecognizeLicensePlate</td>
                    <td>Identifies the license plate information in the input image and returns the coordinates and content of the license plate information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Motor Vehicle Sales Invoice Recognition</td>
                    <td>RecognizeMvsInvoice</td>
                    <td>Recognize motor vehicle sales invoices and used vehicle sales invoices. (The service can automatically distinguish the two types and return the corresponding fields.) Text content in and the recognition result is returned to the user in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Network Image OCR</td>
                    <td>RecognizeWebImage</td>
                    <td>Identifies text in network images and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Passport ID</td>
                    <td>RecognizePassport</td>
                    <td>Identifies the text information in the passport home page image uploaded by the user and returns the structured recognition result. In the current version, all fields of Chinese passports can be identified. Foreign passports support the identification of the two internationally standardized machine-readable codes below the passport, and can extract 6-7 key fields from them.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Invoice Identification</td>
                    <td>RecognizeQuotaInvoice</td>
                    <td>Identifies text information in quota invoices and returns the recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Real Property Certificate Identification</td>
                    <td>RecognizeRealEstateCertificate</td>
                    <td>Identifies the text information in the real estate certificate and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Road Transport License Identification</td>
                    <td>RecognizeTransportationLicense</td>
                    <td>Identifies the text information on the first page of the road transport license and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Road Transport Qualification Certificate Identification</td>
                    <td>RecognizeQualificationCertificate</td>
                    <td>Identifies the key text information on the road transport qualification certificate and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Seal Identification</td>
                    <td>RecognizeSeal</td>
                    <td>Detects and identifies seals in contract files or common bills, erases and extracts seals from images, and returns the results of seal detection, identification, erasing, and extraction in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Smart Document Parsing</td>
                    <td>RecognizeSmartDocumentRecognizer</td>
                    <td>Extracts key-value pairs, recognizes characters, and recognizes tables for documents in any format, such as certificates, receipts, and forms, implementing advanced and efficient automatic and structured return.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Taxi Invoice OCR</td>
                    <td>RecognizeTaxiInvoice</td>
                    <td>Identifies text information in taxi invoices and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Thai Identity Card Recognition</td>
                    <td>RecognizeThailandIdcard</td>
                    <td>Identifies the text information in the Thai ID card and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Thailand License Plate Recognition</td>
                    <td>RecognizeThailandLicensePlate</td>
                    <td>Identifies the license plate information in the Thailand license plate image and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Train ticket recognition</td>
                    <td>RecognizeTrainTicket</td>
                    <td>Identifies text information in train tickets and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VAT Invoice Recognition</td>
                    <td>RecognizeVatInvoice</td>
                    <td>Identifies the type of the VAT invoice and the text content in the image, and returns the recognition result in JSON format. Authenticity verification is not supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VIN code identification</td>
                    <td>RecognizeVin</td>
                    <td>Recognize the vehicle frame number in the image and return the recognition result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Vehicle Certificate Identification</td>
                    <td>RecognizeVehicleCertificate</td>
                    <td>Identifies text information in the vehicle certificate and returns the structured recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Vehicle Toll Invoice OCR</td>
                    <td>RecognizeTollInvoice</td>
                    <td>Identifies text information in a vehicle toll invoice and returns the recognition result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Vicient license recognition</td>
                    <td>RecognizeVehicleLicense</td>
                    <td>Identifies the vehicle license image uploaded by the user. (or the URL of the vehicle license image file on OBS on HUAWEI CLOUD provided by the user) The text content of the homepage and secondary page in the, and the recognition result is returned to the user.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
